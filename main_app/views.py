from django.shortcuts import render

rats = [
  {'name': 'Pixie', 'breed': 'Feeder rat', 'description': 'sweet, loving and a runt', 'age': 1},
  {'name': 'Ralphie', 'breed': 'Rex', 'description': 'confused, social and nosey', 'age': 1.5},
]
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def rats_index(request):
    return render(request, 'rats/index.html', {
        'rats': rats
    })