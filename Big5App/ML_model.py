import os
import django
import pandas as pd
import numpy as np
from scipy.stats import percentileofscore

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
django.setup()

# Load the data
data = pd.read_csv('/Users/ganesh/Documents/GitHub/djangoProject1/djangoProject1/Datasets/BigFive.csv', sep='\t')
data = data.dropna()
df = data.iloc[:, 0:50]

pos_questions = [
    'EXT1','EXT3','EXT5','EXT7','EXT9',
    'EST1','EST3','EST5','EST6','EST7','EST8','EST9','EST10',
    'AGR2','AGR4','AGR6','AGR8','AGR9','AGR10',
    'CSN1','CSN3','CSN5','CSN7','CSN9','CSN10',
    'OPN1','OPN3','OPN5','OPN7','OPN8','OPN9','OPN10',
]

neg_questions = [
    'EXT2','EXT4','EXT6','EXT8','EXT10',
    'EST2','EST4',
    'AGR1','AGR3','AGR5','AGR7',
    'CSN2','CSN4','CSN6','CSN8',
    'OPN2','OPN4','OPN6',
]

df[neg_questions] = 6 - df[neg_questions]

df['Extraversion'] = df.iloc[:, 0:9].mean(axis=1)
df['Neuroticism'] = df.iloc[:, 10:19].mean(axis=1)
df['Agreeableness'] = df.iloc[:, 20:29].mean(axis=1)
df['Conscientiousness'] = df.iloc[:, 30:39].mean(axis=1)
df['Openness'] = df.iloc[:, 40:49].mean(axis=1)

df = df.replace({6: 5, 0: 1})
df['Country'] = data['country']

# Select the last row of the dataset
latest_user_data = df.iloc[-1].to_dict()

# Extract the user's name
#latest_user_name = data.iloc[-1]['name']

# Convert the latest user data to numeric values
latest_user_data = {k: pd.to_numeric(v, errors='coerce') for k, v in latest_user_data.items()}

# Create a DataFrame for the latest user
latest_user = pd.DataFrame(latest_user_data, index=[0])

print(latest_user)

# Calculate the trait scores for the latest user
latest_user['Extraversion'] = latest_user.iloc[:, 0:10].mean(axis=1)
latest_user['Neuroticism'] = latest_user.iloc[:, 10:20].mean(axis=1)
latest_user['Agreeableness'] = latest_user.iloc[:, 20:30].mean(axis=1)
latest_user['Conscientiousness'] = latest_user.iloc[:, 30:40].mean(axis=1)
latest_user['Openness'] = latest_user.iloc[:, 40:50].mean(axis=1)

# Extract the trait scores
latest_user_traits = latest_user[['Extraversion', 'Neuroticism', 'Agreeableness', 'Conscientiousness', 'Openness']]

# Calculate percentiles
percentiles = {}
for trait in latest_user_traits.columns:
    trait_value = latest_user_traits[trait].iloc[0]  # Get the value for the trait
    percentiles[trait] = percentileofscore(df[trait], trait_value)

# Print the user's name and their percentile scores
#print(f"{latest_user_name}'s percentile scores are: {percentiles}")