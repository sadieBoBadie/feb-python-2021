from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    print("In index route")

    return render(request, "index.html")

# action route / process route
def process_form(request):
    print("*"*30)
    print(request.POST)

    context = {
        "first_name": request.POST["first_name"],
        "last_name": request.POST["last_name"],
    }

    if request.POST["comment"]:
        context["comment"] = request.POST["comment"]

    return render(request, "success.html", context)
    