from os import stat
from django.http import JsonResponse
from rest_framework.response import Response
import drinks
from . models import Drinks
from . serializer import DrinksSerializer
from rest_framework.decorators import api_view
from rest_framework import status

from drinks import serializer

@api_view(['GET','POST'])
def detail_view(request):
    if request.method == 'GET':
        drink = Drinks.objects.all()
        serializer = DrinksSerializer(drink,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DrinksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['DELETE','PUT','GET'])
def detail_list(request,id):
    try:
        drink = Drinks.objects.get(pk=id)
    except Drinks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer = DrinksSerializer(drink)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DrinksSerializer(drink,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    