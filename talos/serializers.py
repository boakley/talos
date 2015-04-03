from rest_framework import serializers
from talos.models import Project, Collection, Testcase, Keyword

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ("root",)

class KeywordSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="keyword-detail")
    class Meta:
        model = Keyword
        fields = ("url", "collection", "name", "doc", "args")

class CollectionSerializer(serializers.HyperlinkedModelSerializer):
    keywords = serializers.HyperlinkedRelatedField(view_name="keyword-detail", read_only=True, many=True)
    url = serializers.HyperlinkedIdentityField(view_name="collection-detail")

    class Meta:
        model = Collection
        fields = ("url", "path", "name", "collection_type",
                  "version", "scope", "namedargs", "doc", "doc_format", "keywords")
