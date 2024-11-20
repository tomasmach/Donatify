from django import forms
from .models import DonationGoal

class DonationGoalForm(forms.ModelForm):
    class Meta:
        model = DonationGoal
        fields = ['title', 'description', 'target_amount']
