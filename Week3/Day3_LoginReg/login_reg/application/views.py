from django.shortcuts import render, redirect
import bcrypt
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "index.html")

def registerUser(request):
    
    errors = User.objects.validate(request.POST)

    if errors:
        # put error messages in messages
        for form_field,message in errors.items():
            messages.error(request, message)
        return redirect('/')

    # otherwise...
    pw_hash = bcrypt.hashpw(request.POST.encode(), bcrypt.gensalt()).decode()

    new_user = User.objects.create(
        first_name = request.POST["first_name"],
        last_name = request.POST["last_name"],
        birthday = request.POST["birthday"],
        # YYYY-MM-DD
        email = request.POST["email"],
        password = pw_hash,
    )


    return redirect('/dashboard')

def login(request):

    # pseudocode:
    # Check the database to see if the user exists
    # check the password
        # hash the entered password and check against the DB pw_hash
        # Note: checkpw function does this hashing for you.
    
    user = User.objects.filter(email=request.POST["email"])
    # empty list if not there or a list with one object
    if user:
        # CODE the following:
        # if there is a user, check the password.
            # if pw hashes match put their id in session (log them in)
                # Go to dashboard yay!
        pass # TAKE THIS LINE OUT!

    # (else)
    messages.error(request, "Login failed")

    return redirect('/')