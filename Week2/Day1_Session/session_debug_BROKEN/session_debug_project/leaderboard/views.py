from django.shortcuts import render, redirect

# Create your views here.
def index(request): 

    return render(request, "index.html")


def leaderBoard(request):

    # Redirect to the login page if 
    # they are not logged in
    if "user_name" not in session:
        print('redirecting...')
        return redirect('/')

    ranks = ["first", "second", "third"]

    # If any rank hasn't been assigned yet 
    # initialize the rank in session to 
    #  "Please assign rank." 
    for rank in ranks:
        if rank not in request.session:
            request.session[rank] = 'Please assign a rank.'

    return render(request, "leaderboard.html")

def show(rank):

    name = ""

    if rank == 1:
        if request.session['first'] == "Please assign a rank.":
            return redirect('/dashboard')
        name = request.session['first']
    elif rank == 2:
        name = request.session['second']
    else:
        name = request.session['third']

    return render(request, "showFriend.html", {'rank':rank, 'name': name })

def enter(request):
    print(request.POST)
    name = request.POST["firstName"] + " " + request.POST["lastName"]
    request.session['user_name'] = name
    return redirect('/leaderboard')

def changeRanks(request):

    print(request.POST)

    request.session['first'] = request.POST['first']
    request.session['second'] = request.POST['second']
    request.session['third'] = request.POST['third']

    return redirect('/leaderboard')

def logout(request):
    request.session.clear()
    return redirect('/')