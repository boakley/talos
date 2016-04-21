from django.shortcuts import render
from rest_framework import viewsets
from talos.models import Project, ResourceFile, LibraryFile, Testcase, Keyword, SuiteFile
from talos.serializers import (ProjectSerializer, LibraryFileSerializer, ResourceFileSerializer,
                               KeywordSerializer, TestcaseSerializer, SuiteFileSerializer)
from django.http import HttpResponse


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class LibraryFileViewSet(viewsets.ModelViewSet):
    queryset = LibraryFile.objects.all()
    serializer_class = LibraryFileSerializer

class ResourceFileViewSet(viewsets.ModelViewSet):
    queryset = ResourceFile.objects.all()
    serializer_class = ResourceFileSerializer

class SuiteFileViewSet(viewsets.ModelViewSet):
    queryset = SuiteFile.objects.all()
    serializer_class = SuiteFileSerializer

class TestcaseViewSet(viewsets.ModelViewSet):
    queryset = Testcase.objects.all()
    serializer_class = TestcaseSerializer

class KeywordViewSet(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer

# Application views
# TO DO: add /about to return info about talos
def index(request):
    return HttpResponse("Hello, world!")
