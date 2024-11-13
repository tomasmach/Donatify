from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import DonationGoal

class DonationGoalTests(TestCase):

    def setUp(self):
        # Set up a test user and authenticate the client
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        # Data for creating a donation goal
        self.goal_data = {
            "title": "New Computer",
            "description": "Donation goal for a new computer",
            "target_amount": "5000.00",
            "user": self.user.id  # Explicitly include user
        }

    def test_create_donation_goal(self):
        # Test that a donation goal can be created successfully
        response = self.client.post("/api/donation-goals/", self.goal_data, format='json')
        print("Response data:", response.data)  # Debugging output
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(DonationGoal.objects.count(), 1)
        self.assertEqual(DonationGoal.objects.get().title, "New Computer")

    def test_get_donation_goals(self):
        # Test that a list of donation goals can be retrieved
        self.client.post("/api/donation-goals/", self.goal_data, format='json')
        response = self.client.get("/api/donation-goals/")
        print("Response data:", response.data)  # Debugging output
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "New Computer")

    def test_update_donation_goal(self):
        # Test that a donation goal can be updated successfully
        response = self.client.post("/api/donation-goals/", self.goal_data, format='json')
        goal = DonationGoal.objects.get()

        update_data = {
            "title": "Streaming Computer",
            "description": "Updated description",
            "target_amount": "6000.00",
            "user": self.user.id  # Explicitly include user
        }
        response = self.client.put(f"/api/donation-goals/{goal.id}/", update_data, format='json')
        print("Response data:", response.data)  # Debugging output
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        goal.refresh_from_db()
        self.assertEqual(goal.title, "Streaming Computer")
        self.assertEqual(goal.target_amount, 6000.00)

    def test_delete_donation_goal(self):
        # Test that a donation goal can be deleted successfully
        response = self.client.post("/api/donation-goals/", self.goal_data, format='json')
        goal = DonationGoal.objects.get()

        response = self.client.delete(f"/api/donation-goals/{goal.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(DonationGoal.objects.count(), 0)
