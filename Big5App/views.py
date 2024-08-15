from django.shortcuts import render, redirect
#from .forms import AssessmentForm1, AssessmentForm2, AssessmentForm3, AssessmentForm4, AssessmentForm5
from .forms import AssessmentForm1
from .models import AssessmentResponse
import uuid
import pandas as pd
import numpy as np
from scipy.spatial.distance import euclidean
import os
import django
import sqlite3
from scipy.stats import percentileofscore

def home(request):
    return render(request, 'index.html')

def store_name(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        request.session['name'] = name
        request.session['user_id'] = str(uuid.uuid4())
        return redirect('assessment')
    return HttpResponse("Invalid request method", status=405)


def assessment(request):
    if request.method == 'POST':
        form = AssessmentForm1(request.POST)
        if form.is_valid():
            # Print the cleaned data to check what is being processed
            #print("Cleaned Data:", form.cleaned_data)
            response, created = AssessmentResponse.objects.get_or_create(
                user_id=request.session.get('user_id'),
                defaults={'name': request.session.get('name', 'Guest')}
            )
            for field in form.fields:
                setattr(response, field, form.cleaned_data[field])
            response.save()
            return redirect('success')
            #return redirect('assessment2')
    else:
        form = AssessmentForm1()
    return render(request, 'assessment_all.html', {'form': form})
def analysis_view(request):
    # Load the data
    data = pd.read_csv('/Users/ganesh/Documents/GitHub/djangoProject1/djangoProject1/Datasets/BigFive.csv', sep='\t')
    data = data.dropna()
    df = data.iloc[:, 0:50]

    pos_questions = [
        'EXT1', 'EXT3', 'EXT5', 'EXT7', 'EXT9',
        'EST1', 'EST3', 'EST5', 'EST6', 'EST7', 'EST8', 'EST9', 'EST10',
        'AGR2', 'AGR4', 'AGR6', 'AGR8', 'AGR9', 'AGR10',
        'CSN1', 'CSN3', 'CSN5', 'CSN7', 'CSN9', 'CSN10',
        'OPN1', 'OPN3', 'OPN5', 'OPN7', 'OPN8', 'OPN9', 'OPN10',
    ]

    neg_questions = [
        'EXT2', 'EXT4', 'EXT6', 'EXT8', 'EXT10',
        'EST2', 'EST4',
        'AGR1', 'AGR3', 'AGR5', 'AGR7',
        'CSN2', 'CSN4', 'CSN6', 'CSN8',
        'OPN2', 'OPN4', 'OPN6',
    ]

    # Reverse scoring for negative questions
    df[neg_questions] = 6 - df[neg_questions]
    df['Extraversion'] = df.iloc[:, 0:10].mean(axis=1)
    df['Neuroticism'] = df.iloc[:, 10:20].mean(axis=1)
    df['Agreeableness'] = df.iloc[:, 20:30].mean(axis=1)
    df['Conscientiousness'] = df.iloc[:, 30:40].mean(axis=1)
    df['Openness'] = df.iloc[:, 40:50].mean(axis=1)
    df = df.replace({6: 5, 0: 1})
    df['Country'] = data['country']

    # Setup Django environment (if needed)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
    django.setup()

    # Connect to the database
    db_path = '/Users/ganesh/Documents/GitHub/djangoProject/db.sqlite3'
    conn = sqlite3.connect(db_path)
    user_id = request.session.get('user_id')

    # Query to get the latest user data
    query = """
    SELECT * FROM Big5App_assessmentresponse 
    WHERE user_id = ?
    """
    latest_user = pd.read_sql_query(query, conn, params=[user_id])

    if latest_user.empty:
        return {
            'error': 'No data found for the latest user.',
            'user_name': request.session.get('name', 'Guest')
        }

    # Calculate mean scores for the latest user
    latest_user['Extraversion'] = latest_user.iloc[:, 1:11].mean(axis=1)
    latest_user['Neuroticism'] = latest_user.iloc[:, 11:21].mean(axis=1)
    latest_user['Agreeableness'] = latest_user.iloc[:, 21:31].mean(axis=1)
    latest_user['Conscientiousness'] = latest_user.iloc[:, 31:41].mean(axis=1)
    latest_user['Openness'] = latest_user.iloc[:, 41:51].mean(axis=1)
    new_user_traits = latest_user[['Extraversion', 'Neuroticism', 'Agreeableness', 'Conscientiousness', 'Openness']]

    # Calculate percentiles
    percentiles = {}
    for trait in new_user_traits.columns:
        trait_value = new_user_traits[trait].iloc[0]
        percentiles[trait] = percentileofscore(df[trait], trait_value)

    # Find the closest countries
    country_means = df.groupby('Country')[
        ['Extraversion', 'Neuroticism', 'Agreeableness', 'Conscientiousness', 'Openness']].mean()
    distances = country_means.apply(lambda row: euclidean(row, new_user_traits.iloc[0]), axis=1)
    top_countries = distances.nsmallest(5).index.tolist()

    # Calculate mean scores
    new_user_mean_scores = new_user_traits.mean()
    all_users_mean_scores = df[['Extraversion', 'Neuroticism', 'Agreeableness', 'Conscientiousness', 'Openness']].mean()

    # Print statements for debugging
    print("Percentiles:", percentiles)
    print("Top Countries:", top_countries)
    print("New User Mean Scores:", new_user_mean_scores)
    print("All Users Mean Scores:", all_users_mean_scores)
    print("User Name:", request.session.get('name', 'Guest'))

    context = {
        'percentiles': percentiles,
        'top_countries': top_countries,
        'new_user_mean_scores': new_user_mean_scores.to_dict(),  # Convert Series to dict
        'all_users_mean_scores': all_users_mean_scores.to_dict(),  # Convert Series to dict
        'user_name': request.session.get('name', 'Guest')
    }

    return context


def success(request):
    context = analysis_view(request)
    return render(request, 'success_backup.html', context)