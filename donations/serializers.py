from rest_framework import serializers
from .models import DonationGoal

class DonationGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationGoal
        fields = '__all__'