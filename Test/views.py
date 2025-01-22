from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import TutorsForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def loginPage(request):
    if request.method == 'POST':
        form = TutorsForm(request.POST)
        name=request.POST.get('name')
        department=request.POST.get('department')
        staff_number=request.POST.get('staff_number')

        user=authenticate(request, name=name,department=department,staff_number=staff_number)


    return render(request, 'login.html')

def logoutUser(request):
    return HttpResponse("the logout page")



def Homepage(request):
    return render(request,'home.html')



def registerPage(request):
    if request.method == 'POST':
        form = TutorsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('home')
    else:
        form = TutorsForm()
    return render(request, 'register.html',{'form': form})



def Homepage(request):
    return render(request,'home.html')

