from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *



class ListTodo(generics.ListAPIView):

    serializer_class=ToDoSerializer
    queryset=ToDo.objects.all()

class DetailsTodo(generics.RetrieveUpdateAPIView):

    serializer_class=ToDoSerializer
    queryset=ToDo.objects.all()
class CreateTodo(generics.CreateAPIView):
    serializer_class=ToDoSerializer
    queryset=ToDo.objects.all()
class DeleteTodo(generics.DestroyAPIView):
        serializer_class=ToDoSerializer
        queryset=ToDo.objects.all()
