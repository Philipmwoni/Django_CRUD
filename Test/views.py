from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def loginPage(request):
    return render(request, 'login.html')

def logoutUser(request):
    return HttpResponse("the logout page")

def registerPage(request):
    return HttpResponse("register for your account")
def Homepage(request):
    return render(request,'home.html')

