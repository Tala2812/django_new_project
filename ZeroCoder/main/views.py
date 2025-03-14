from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def data(request):
    return render(request, 'main/data.html')

def test(request):
    return render(request, 'main/test.html')

def facts(request):
    return render(request, 'main/facts.html')
