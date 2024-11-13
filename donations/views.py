from rest_framework import viewsets, permissions
from .models import DonationGoal
from .serializers import DonationGoalSerializer

class DonationGoalViewSet(viewsets.ModelViewSet):
    queryset = DonationGoal.objects.all()
    serializer_class = DonationGoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Assign the current user as the owner of the donation goal upon creation
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
