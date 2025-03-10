from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth import login, authenticate, logout # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.contrib import messages # type: ignore
from .forms import UserRegistrationStep1Form, UserRegistrationStep2Form, CustomLoginForm, ManualUserRegistrationForm
from .models import CustomUser

def register_step1(request):
    if request.method == 'POST':
        form = UserRegistrationStep1Form(request.POST)
        if form.is_valid():
            # Store form data in session
            request.session['user_data'] = {
                'id_number': form.cleaned_data['id_number'],
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email'],
                'faculty': form.cleaned_data['faculty'],
                'user_category': form.cleaned_data['user_category'].id
            }
            return redirect('register_step2')
        else:
            # Add form errors to messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserRegistrationStep1Form()
    
    return render(request, 'accounts/register_step1.html', {'form': form})

def register_step2(request):
    if 'user_data' not in request.session:
        messages.error(request, "Please complete step 1 first")
        return redirect('register_step1')
    
    if request.method == 'POST':
        form = UserRegistrationStep2Form(request.POST)
        if form.is_valid():
            try:
                user_data = request.session['user_data']
                user = form.save(commit=False)
                user.id_number = user_data['id_number']
                user.first_name = user_data['first_name']
                user.last_name = user_data['last_name']
                user.email = user_data['email']
                user.faculty = user_data['faculty']
                user.user_category_id = user_data['user_category']
                user.username = user_data['id_number']  # Using ID as username
                user.save()
                
                del request.session['user_data']
                return redirect('login')
            except Exception as e:
                messages.error(request, f"Error creating user: {str(e)}")
        else:
            # Add form errors to messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserRegistrationStep2Form()
    
    return render(request, 'accounts/register_step2.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            id_number = form.cleaned_data['id_number']
            password = form.cleaned_data['password']
            user = authenticate(request, username=id_number, password=password)
            if user is not None:
                login(request, user)
                return redirect('users')
            else:
                form.add_error(None, 'Invalid ID number or password')
    else:
        form = CustomLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def users_view(request):
    users = CustomUser.objects.all()
    context = {
        'users': users,
        'active_tab': 'users'  # For highlighting the active sidebar item
    }
    return render(request, 'accounts/users.html', context)

@login_required
def add_user(request):
    if request.method == 'POST':
        form = ManualUserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.username = form.cleaned_data['id_number']  # Use ID as username
                user.set_password(form.cleaned_data['password'])
                user.save()
                return redirect('users')
            except Exception as e:
                messages.error(request, f'Error al crear usuario: {str(e)}')
    else:
        form = ManualUserRegistrationForm()
    
    return render(request, 'accounts/add_user.html', {'form': form})