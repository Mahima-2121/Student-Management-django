from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
     class Meta:
        model  = Student
        fields = [
            'first_name', 'last_name', 'roll_number',
            'email', 'phone', 'gender',
            'date_of_birth', 'course', 'is_active',
        ]
        widgets = {
            'date_of_birth': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }