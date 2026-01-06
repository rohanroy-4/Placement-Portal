from django.contrib.auth import logout
from django.shortcuts import redirect

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('dashboard')
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            email=request.POST['email'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'accounts/login.html')

def dashboard(request):
    if request.user.role == 'student':
        return render(request, 'accounts/student_dashboard.html')
    if request.user.role == 'company':
        return render(request, 'accounts/company_dashboard.html')
    return render(request, 'accounts/admin_dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')
