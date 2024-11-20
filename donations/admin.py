from django.contrib import admin
from .models import DonationGoal

@admin.register(DonationGoal)
class DonationGoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'target_amount', 'collected_amount', 'created_at', 'completed')
    list_filter = ('completed', 'created_at')
    search_fields = ('title', 'description')
