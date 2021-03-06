from django import forms
from .models import Subject2,Help

class Subject2Form(forms.ModelForm):

    class Meta:
        model = Subject2
        fields = ('what_you_are_teaching', 'subject', 'author','experience','photo','date_posted',)

class HelpForm(forms.ModelForm):

    class Meta:
        model = Help
        fields = ('name', 'subject_name', 'body',)