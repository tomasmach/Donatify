from rest_framework import serializers
from .models import DonationGoal

class DonationGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationGoal
        fields = ['id', 'user', 'title', 'description', 'target_amount', 'collected_amount', 'created_at', 'completed']
        read_only_fields = ['id', 'created_at', 'collected_amount', 'completed']

    # Validate that target_amount is greater than 0
    def validate_target_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Target amount must be greater than 0.")
        return value

    # Validate that title is not empty
    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value
