from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import pet
from .serializers import petSerializer

# Create your views here.

@api_view(['GET' , 'POST'])
def pet_list(request):
    if request.method == 'GET':
        pets = pet.objects.all()
        serializer = petSerializer(pets, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = petSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400)
    

@api_view(['GET', 'PUT', 'DELETE'])
def pet_detail(request, pk):
    try:
        Pet = pet.objects.get(pk=pk)
    except pet.DoesNotExist:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = petSerializer(pet)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = petSerializer(pet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        pet.delete()
        return Response(status=204)
    