from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import TutorsForm,SubjectsForm,StudentsForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def loginPage(request):
    if request.method == 'POST':
        form = TutorsForm(request.POST)
        name=request.POST.get('name')
        department=request.POST.get('department')
        staff_number=request.POST.get('staff_number')

        user=authenticate(request, name=name,department=department,staff_number=staff_number)
        if user is not None:
            login(request, user)



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


@login_required(login_url='login')
def Entermarks(request):
    if request.method == 'POST':
        form = SubjectsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'successfully submitted!')
            return redirect('home')
        else:
            messages.error(request, 'invalid input please try again')
            form = SubjectsForm()
    return render(request,'marks.html')