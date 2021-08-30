from django.contrib.auth import authenticate, login
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.models import User


""" User account creation """
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, f"Welcome, {username}")
            return redirect('profile')           
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})


""" User profile """
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
    
    context = {
        'u_form':u_form,
    }

    return render(request, 'users/profile.html', context)


""" User public profile """
@login_required
def public_profile(request, pk):
    other_user = get_object_or_404(User, pk=pk)
    context = {
        "cuser": other_user
    }
    return render(request, 'users/public_profile.html', context)


""" Search by username """
def search(request):
    query = request.GET['query']
    if len(query) >= 250 or len(query) < 1:
        return HttpResponse("Query too large")
    elif len(query.strip()) == 0:
        users = User.objects.none()
    else:
        users = User.objects.filter(username__icontains = query)
    
    params = {'users': users}
    return render(request, 'users/search_results.html', params)