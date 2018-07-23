from django.shortcuts import render

# Create your views here.
def appmain(request):
    return render(request, 'quiz/main.html', {})

def fifamain(request):
    return render(request, 'quiz/fifa.html', {})
