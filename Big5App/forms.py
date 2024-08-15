from django import forms
from .models import AssessmentResponse


class BaseAssessmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

    def clean(self):
        cleaned_data = super().clean()
        for field in self.fields:
            if cleaned_data.get(field) is None:
                cleaned_data[field] = 3
        return cleaned_data


class AssessmentForm1(BaseAssessmentForm):
    class Meta:
        model = AssessmentResponse
        fields = ['EXT1', 'EXT2', 'EXT3', 'EXT4', 'EXT5', 'EXT6', 'EXT7', 'EXT8', 'EXT9', 'EXT10',
                  'EST1', 'EST2', 'EST3', 'EST4', 'EST5', 'EST6', 'EST7', 'EST8', 'EST9', 'EST10',
                  'AGR1', 'AGR2', 'AGR3', 'AGR4', 'AGR5', 'AGR6', 'AGR7', 'AGR8', 'AGR9', 'AGR10',
                  'CSN1', 'CSN2', 'CSN3', 'CSN4', 'CSN5', 'CSN6', 'CSN7', 'CSN8', 'CSN9', 'CSN10',
                  'OPN1', 'OPN2', 'OPN3', 'OPN4', 'OPN5', 'OPN6', 'OPN7', 'OPN8', 'OPN9', 'OPN10']
        widgets = {field: forms.RadioSelect(choices=[(i,
                                                     f"{i} - {'Disagree' if i == 1 else 'Slightly Disagree' if i == 2 else 'Neutral' if i == 3 else 'Slightly Agree' if i == 4 else 'Agree'}")
                                                     for i in range(1, 6)])
                   for field in fields}

'''
class AssessmentForm1(BaseAssessmentForm):
    class Meta:
        model = AssessmentResponse
        fields = ['EXT1', 'EXT2', 'EXT3', 'EXT4', 'EXT5', 'EXT6', 'EXT7', 'EXT8', 'EXT9', 'EXT10']
        widgets = {f'EXT{i}': forms.RadioSelect(choices=[(i,
                                                          f"{i} - {'Disagree' if i == 1 else 'Slightly Disagree' if i == 2 else 'Neutral' if i == 3 else 'Slightly Agree' if i == 4 else 'Agree'}")
                                                         for i in range(1, 6)]) for i in range(1, 11)}

class AssessmentForm2(BaseAssessmentForm):
    class Meta:
        model = AssessmentResponse
        fields = ['EST1', 'EST2', 'EST3', 'EST4', 'EST5', 'EST6', 'EST7', 'EST8', 'EST9', 'EST10']
        widgets = {f'EST{i}': forms.RadioSelect(choices=[(i,
                                                          f"{i} - {'Disagree' if i == 1 else 'Slightly Disagree' if i == 2 else 'Neutral' if i == 3 else 'Slightly Agree' if i == 4 else 'Agree'}")
                                                         for i in range(1, 6)]) for i in range(1, 11)}


class AssessmentForm3(BaseAssessmentForm):
    class Meta:
        model = AssessmentResponse
        fields = ['AGR1', 'AGR2', 'AGR3', 'AGR4', 'AGR5', 'AGR6', 'AGR7', 'AGR8', 'AGR9', 'AGR10']
        widgets = {f'AGR{i}': forms.RadioSelect(choices=[(i,
                                                          f"{i} - {'Disagree' if i == 1 else 'Slightly Disagree' if i == 2 else 'Neutral' if i == 3 else 'Slightly Agree' if i == 4 else 'Agree'}")
                                                         for i in range(1, 6)]) for i in range(1, 11)}


class AssessmentForm4(BaseAssessmentForm):
    class Meta:
        model = AssessmentResponse
        fields = ['CSN1', 'CSN2', 'CSN3', 'CSN4', 'CSN5', 'CSN6', 'CSN7', 'CSN8', 'CSN9', 'CSN10']
        widgets = {f'CSN{i}': forms.RadioSelect(choices=[(i,
                                                          f"{i} - {'Disagree' if i == 1 else 'Slightly Disagree' if i == 2 else 'Neutral' if i == 3 else 'Slightly Agree' if i == 4 else 'Agree'}")
                                                         for i in range(1, 6)]) for i in range(1, 11)}


class AssessmentForm5(BaseAssessmentForm):
    class Meta:
        model = AssessmentResponse
        fields = ['OPN1', 'OPN2', 'OPN3', 'OPN4', 'OPN5', 'OPN6', 'OPN7', 'OPN8', 'OPN9', 'OPN10']
        widgets = {f'OPN{i}': forms.RadioSelect(choices=[(i,
                                                          f"{i} - {'Disagree' if i == 1 else 'Slightly Disagree' if i == 2 else 'Neutral' if i == 3 else 'Slightly Agree' if i == 4 else 'Agree'}")
                                                         for i in range(1, 6)]) for i in range(1, 11)}
'''
