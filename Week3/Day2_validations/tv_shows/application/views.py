from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

# Create your views here.

def dashboard(request):
    context = {
        "shows": Show.objects.all()
    }
    return render(request, "dashboard.html", context)

def new_page(request):
    return render(request, "new.html")

def edit_page(request, show_id):
    # GET THE SHOW FROM THE DB
    context = {
        "show": Show.objects.get(id=show_id)
    }
    print("edit show id: ", show_id)
    return render(request, "edit.html", context)

def show_page(request, show_id):
    # GET THE SHOW FROM THE DB
    print("show page id: ", show_id)
    context = {
        "show": Show.objects.get(id=show_id)
    }

    return render(request, "show.html", context)


# Action and Post routes (will redirect)
def delete(request, show_id):
    print("delete show id: ", show_id)
    # delete something in the db!
    return redirect('/shows')

def create_show(request):
    print("Create show from form function")
    print(request.POST)

    errors = Show.objects.basic_validator(request.POST)

    if errors:
        for category, message in errors.items():
            messages.error(request, message)
        return redirect('/shows/new')

    show = Show.objects.create(
        title = request.POST['title'],
        description = request.POST['title'],
        network = request.POST['title'],
        release_date = request.POST['title']
    )

    return redirect(f'/shows/{show.id}')

def update(request, show_id):
    print("Update show in DB function")
    print(request.POST)

    errors = Show.objects.basic_validator(request.POST)

    if errors:
        for category, message in errors.items():
            messages.error(request, message)
        return redirect(f'/shows/{show_id}/edit')

    show_to_update = Show.objects.get(id=show_id)
    show_to_update.title = request.POST["title"]
    show_to_update.release_date = request.POST["release_date"]
    show_to_update.description = request.POST["description"]
    show_to_update.network = request.POST["network"]

    return redirect(f'/shows/{show_id}')

