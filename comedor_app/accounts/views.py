from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth import login, authenticate # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from .forms import UserRegistrationStep1Form, UserRegistrationStep2Form, CustomLoginForm

def register_step1(request):
    if request.method == 'POST':
        form = UserRegistrationStep1Form(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            request.session['user_data'] = {
                'id_number': form.cleaned_data['id_number'],
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email'],
                'faculty': form.cleaned_data['faculty'],
                'is_employee': form.cleaned_data['is_employee']
            }
            return redirect('register_step2')
    else:
        form = UserRegistrationStep1Form()
    return render(request, 'accounts/register_step1.html', {'form': form})

def register_step2(request):
    if 'user_data' not in request.session:
        return redirect('register_step1')
    
    if request.method == 'POST':
        form = UserRegistrationStep2Form(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user_data = request.session['user_data']
            user.id_number = user_data['id_number']
            user.first_name = user_data['first_name']
            user.last_name = user_data['last_name']
            user.email = user_data['email']
            user.faculty = user_data['faculty']
            user.is_employee = user_data['is_employee']
            user.username = user_data['id_number']  # Using ID as username
            user.save()
            del request.session['user_data']
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationStep2Form()
    return render(request, 'accounts/register_step2.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            id_number = form.cleaned_data['id_number']
            password = form.cleaned_data['password']
            user = authenticate(request, username=id_number, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CustomLoginForm()
    return render(request, 'accounts/login.html', {'form': form})