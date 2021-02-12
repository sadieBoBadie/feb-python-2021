from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    print("**********************")
    print(request.path_info)
    print(request.method)
    return HttpResponse("Testing")

def greet(request, num):
    kitties = [
        {"name": "Nozick", "age": 7},
        {"name": "Bateson", "age": 7},
        {"name": "Fooder", "age": 20},
        {"name": "Paris", "age": 3},
    ]

    context = {
        "num": num, 
        "kitties": kitties
    }

    return render(request, "index.html", context)