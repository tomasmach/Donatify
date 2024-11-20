from rest_framework import viewsets, permissions
from .models import DonationGoal
from .serializers import DonationGoalSerializer
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import DonationGoalForm
from django.http import JsonResponse

class DonationGoalViewSet(viewsets.ModelViewSet):
    queryset = DonationGoal.objects.all()
    serializer_class = DonationGoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Assign the current user as the owner of the donation goal upon creation
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@login_required
def donation_goal_list(request):
    # Pokud je požadavek AJAX, vrať data ve formátu JSON
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        donation_goals = DonationGoal.objects.filter(user=request.user)
        data = [
            {
                'id': goal.id,
                'title': goal.title,
                'description': goal.description,
                'target_amount': str(goal.target_amount),
                'collected_amount': str(goal.collected_amount),
                'completed': goal.completed,
            }
            for goal in donation_goals
        ]
        return JsonResponse(data, safe=False)

    # Pro normální GET požadavek vrať šablonu
    return render(request, 'donations/donation_goal_list.html')

@login_required
def donation_goal_detail(request, pk):
    donation_goal = get_object_or_404(DonationGoal, pk=pk, user=request.user)
    return render(request, 'donations/donation_goal_detail.html', {'donation_goal': donation_goal})

@login_required
def donation_goal_create(request):
    if request.method == 'POST':
        form = DonationGoalForm(request.POST)
        if form.is_valid():
            donation_goal = form.save(commit=False)
            donation_goal.user = request.user
            donation_goal.save()
            return redirect('donation_goal_list')
    else:
        form = DonationGoalForm()
    return render(request, 'donations/donation_goal_form.html', {'form': form})

@login_required
def donation_goal_update(request, pk):
    donation_goal = get_object_or_404(DonationGoal, pk=pk, user=request.user)
    if request.method == 'POST':
        form = DonationGoalForm(request.POST, instance=donation_goal)
        if form.is_valid():
            form.save()
            return redirect('donation_goal_list')
    else:
        form = DonationGoalForm(instance=donation_goal)
    return render(request, 'donations/donation_goal_form.html', {'form': form})

@login_required
def donation_goal_delete(request, pk):
    donation_goal = get_object_or_404(DonationGoal, pk=pk, user=request.user)
    if request.method == 'POST':
        donation_goal.delete()
        return redirect('donation_goal_list')
    return render(request, 'donations/donation_goal_confirm_delete.html', {'donation_goal': donation_goal})
