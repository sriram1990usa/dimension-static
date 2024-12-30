from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request, 'app/index.html')

def intro(request):
    return render (request, 'app/intro.html')

def work(request):
    return render (request, 'app/work.html')

def about(request):
    return render (request, 'app/about.html')

def contact(request):
    return render (request, 'app/contact.html')

def elements(request):
    return render (request, 'app/elements.html')

def message(request):
    return render (request, 'app/message.html')



