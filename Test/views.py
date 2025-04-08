from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SubjectsForm
from Tutors.models import Tutorform
from .models import Students
from .serializers import StudentsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# API ENDPOINTS

@api_view(['GET', 'POST'])
def Students_list_create(request):
    if request.method == 'GET':
        students = Students.objects.all()
        serializer = StudentsSerializer(Students, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def Students_update_delete(request, pk):
    try:
        student = Students.objects.get(pk=pk)

    except Students.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentsSerializer(Students)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentsSerializer(Students, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Students.objects.get(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Create your views here.
def loginPage(request):
    return render(request, 'login.html')


def logoutUser(request):
    return HttpResponse("the logout page")


def Homepage(request):
    return render(request, 'home.html')


def registerPage(request):
    form = TutorsForm
    if request.method == 'POST':
        form = TutorsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('home')
    else:
        form = TutorsForm()
    return render(request, 'register.html', {'form': form})


def Homepage(request):
    return render(request, 'home.html')


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
    return render(request, 'marks.html')
