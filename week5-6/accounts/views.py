from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import User
# Create your views here.

def register(request):
    if request.method == 'POST':
        User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password'],
            role=request.post['role']
        )
        return redirect('login')
    return render(request, register.html)

@login_required
def dashboard(request):
    user = request.user

    if user.role == 'admin':
        return redirect('admin_page')
    elif user.role == 'staff':
        return redirect('staff_page')
    else: 
        return redirect('user_page')

@login_required
def admin_page(request):
    if request.user.role != 'admin':
        return redirect('dashboard')
    return render(request, 'admin.html')
@login_required
def staff_page(request):
    if request.user.role != 'staff':
        return redirect('dashboard')
    return render(request, 'staff.html')

@login_required
def user_page(request):
    if request.user.role != 'user':
        return redirect('dashboard')
    return render(request, 'user.html')