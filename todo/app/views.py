from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *

# Create your views here.
def main(request):
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        obj1 = UserProfile(name=name, email=email, phone=phone, dob=dob)
        obj1.save()

    # Fetch all UserProfile objects
    obj = UserProfile.objects.all()

    # Correct the context: pass a dictionary
    return render(request, "main.html", {"det": obj})

def delete_user(request, user_id):
    # Fetch the user object using the id passed from the URL
    user_to_delete = get_object_or_404(UserProfile, id=user_id)
    
    # Delete the object
    user_to_delete.delete()

    # Redirect back to the main page after deletion
    return redirect('main')  # Make sure 'main' is the name of the URL fo