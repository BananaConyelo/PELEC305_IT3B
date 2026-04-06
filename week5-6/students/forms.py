from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'email', 'age', 'profile_picture']
    
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18:
            raise forms.ValidationError('Students must be 18+')
        return age
    