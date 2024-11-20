from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from donations.views import DonationGoalViewSet
from donations import views as donation_views

router = routers.DefaultRouter()
router.register(r'donation-goals', DonationGoalViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('donation-goals/', donation_views.donation_goal_list, name='donation_goal_list'),
    path('donation-goals/<int:pk>/', donation_views.donation_goal_detail, name='donation_goal_detail'),
    path('donation-goals/create/', donation_views.donation_goal_create, name='donation_goal_create'),
    path('donation-goals/<int:pk>/edit/', donation_views.donation_goal_update, name='donation_goal_update'),
    path('donation-goals/<int:pk>/delete/', donation_views.donation_goal_delete, name='donation_goal_delete'),
]
