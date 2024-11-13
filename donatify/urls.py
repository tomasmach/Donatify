from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from donations.views import DonationGoalViewSet

router = routers.DefaultRouter()
router.register(r'donation-goals', DonationGoalViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
