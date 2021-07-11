from django import forms
from polls.models import PollQuestion
from . import models


class PollForm(forms.ModelForm):
    question = forms.CharField(label="Write Your Question Here", max_length=200,
                               widget=forms.Textarea(attrs={'rows': 3}))
    option_one = forms.CharField(label="Option one", max_length=200, widget=forms.Textarea(attrs={'rows': 3}))
    option_two = forms.CharField(label="Option Two", max_length=200, widget=forms.Textarea(attrs={'rows': 3}))
    option_three = forms.CharField(label="Option Three", max_length=200, widget=forms.Textarea(attrs={'rows': 3}))
    option_four = forms.CharField(label="Option Four", max_length=200, widget=forms.Textarea(attrs={'rows': 3}))

    class Meta:
        model = models.PollQuestion
        fields = ['question', 'option_one', 'option_two', 'option_three', 'option_four']
