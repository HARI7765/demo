from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)  # Log the user in
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "index.html")


def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        
        # Validation checks
        if not all([username, email, password, confirmpassword]):
            messages.error(request, 'All fields are required.')
        elif confirmpassword != password:
            messages.error(request, "Passwords do not match")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            # Create new user
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Account created successfully")
            return redirect("index")
    # Handle GET request (first visit to signup page)
    return render(request, "signup.html")


def home(request):
    return render(request, "home.html")
