from django.db.migrations import serializer
from django.shortcuts import render
from .models import Tutor
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import TutorSerializer


# API ENDPOINTS

@api_view(['GET', 'POST'])
def tutor_list(request):
    if request.method == 'GET':
        tutors = Tutor.objects.all()
        serializer = TutorSerializer(
            tutors, many=True
        )
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TutorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def tutor_detail(request, pk):
    try:
        tutor = Tutor.objects.get(pk=pk)
    except Tutor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TutorSerializer(tutor)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TutorSerializer(Tutor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        tutor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
