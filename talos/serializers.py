from rest_framework import serializers
from talos.models import Project, Collection, Testcase, Keyword

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ("root",)

class CollectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Collection
        fields = ("project", "path", "name", "collection_type",
                  "version", "scope", "namedargs", "doc", "doc_format")

        
