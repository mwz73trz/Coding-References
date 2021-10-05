from django import forms
from .models import Subject

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['title']

# class ProgramForm(forms.ModelForm):
#     class Meta:
#         model = Program
#         fields = ['name', 'description', 'notes', 'link', 'date_created']