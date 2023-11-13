from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
from .models import Task
from .serializers import TaskSerializer


class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        # Récupérer le paramètre d'ordonnancement de la requête
        ordering = self.request.query_params.get('ordering', 'due_time')

        # Récupérer le paramètre d'ordre (ascendant ou descendant)
        # Par ordre ascendant par défaut.
        order_by = '-' + ordering if self.request.query_params.get('order') == 'desc' else ordering

         # Ici, c'est pour permettre le tri par nom, importance et date d'echéance
        allowed_fields = ['due_time', 'name', 'importance']  # Ajoutez d'autres champs si nécessaire
        if ordering not in allowed_fields:
            ordering = 'due_time'

        # Appliquer la logique de tri
        queryset = Task.objects.filter(completed=False).order_by(ordering)

        return queryset

    def perform_create(self, serializer):
        # Assurez-vous que la nouvelle tâche n'est pas marquée comme complétée par défaut
        serializer.save(completed=False)



class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.filter(completed=False)
    serializer_class = TaskSerializer

class CompletedTaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        # Appliquer la logique pour récupérer les tâches complétées
        queryset = Task.objects.filter(completed=True)
        return queryset

class SearchTasksView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        # Récupérer le paramètre de recherche de la requête
        query = self.kwargs['query']
        
        # Appliquer la logique de recherche
        tasks = Task.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        return tasks