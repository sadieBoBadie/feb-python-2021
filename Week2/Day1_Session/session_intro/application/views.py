from django.shortcuts import render, redirect

# Create your views here.

# request.session = {}

# RENDER Routes/Functions
def index(request):
    print("inside index/root page function")
    # I have no idea about other function
    # calls before me!!
    return render(request, "index.html")

def success(request):
    print("inside success function")
    if 'first_name' in request.session:
        return render(request, "success.html")
    # Want to show info from the form
    # on the success page
    return redirect('/')
    


# REDIRECTING - Action Routes/Functions - 
# POST Routes -- from a form 
# GET -- Deleting or Clearing session
def login(request):
    print(request.POST)

    # Getting info from form

    request.session["first_name"] = request.POST["first_name"]
    request.session["last_name"] = request.POST["last_name"]
    request.session["email"] = request.POST["email"]


    return redirect('/success')

def logout(request):
    request.session.clear()

    return redirect('/')
