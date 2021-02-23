from django.shortcuts import render, redirect
from .models import Dojo, Ninja

# Create your views here.

def index(request):
    print("in index")

    context = {
        "all_dojos": Dojo.objects.all(),
    }

    return render(request, "index.html", context)

def create_dojo(request):
    print("Creating dojo...")
    print(request.POST)

    # Create a dojo with the form info
    Dojo.objects.create(
        name=request.POST["name"],
        city=request.POST["city"],
        state=request.POST["state"],
    )

    return redirect('/')

def create_ninja(request):
    print("Creating ninja...")
    print(request.POST)
    this_dojo = Dojo.objects.get(id=request.POST["dojo_id"])
    Ninja.objects.create(
        first_name=request.POST["first_name"], 
        last_name=request.POST["last_name"],
        dojo = this_dojo,
        )

    return redirect('/')