from django.shortcuts import render
from rest_framework import viewsets
from talos.models import Project, Collection, Testcase, Keyword
from talos.serializers import ProjectSerializer, CollectionSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

