from django.shortcuts import render

# Create your views here.
# mene yeh code likha hai
# from django.http import HttpResponse

def home(request):
    username = "Pawan"
    context = {'username': username} 
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


