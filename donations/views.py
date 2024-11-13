from rest_framework import viewsets
from .models import DonationGoal
from .serializers import DonationGoalSerializer

class DonationGoalViewSet(viewsets.ModelViewSet):
    queryset = DonationGoal.objects.all()
    serializer_class = DonationGoalSerializer