from rest_framework import serializers
from talos.models import Project, LibraryFile, ResourceFile, Testcase, Keyword

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ("root",)

class TestcaseSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="testcase-detail")
    class Meta:
        model = Testcase
        fields = ("url", "parent", "name")

class KeywordSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name="keyword-detail")
    class Meta:
        model = Keyword
#        fields = ("url", "content_object", "name", "doc", "args")
        fields = ("url", "name", "doc", "args")

class LibraryFileSerializer(serializers.HyperlinkedModelSerializer):

    keywords = serializers.HyperlinkedRelatedField(view_name="keyword-detail", read_only=True, many=True)
    url = serializers.HyperlinkedIdentityField(view_name="libraryfile-detail")

    class Meta:
        model = LibraryFile
        fields = ("url", "path", "name", "doc", "doc_format", "keywords",
                  "version", "scope", "namedargs")

class SuiteFileSerializer(serializers.HyperlinkedModelSerializer):
    keywords = serializers.HyperlinkedRelatedField(view_name="keyword-detail", read_only=True, many=True)
    testcases = serializers.HyperlinkedRelatedField(view_name="testcase-detail", read_only=True, many=True)
    url = serializers.HyperlinkedIdentityField(view_name="suitefile-detail")

    class Meta:
        model = LibraryFile
        fields = ("url", "path", "name", "doc", "doc_format", "keywords", "testcases")

class ResourceFileSerializer(serializers.HyperlinkedModelSerializer):
    keywords = serializers.HyperlinkedRelatedField(view_name="keyword-detail", read_only=True, many=True)
    url = serializers.HyperlinkedIdentityField(view_name="resourcefile-detail")

    class Meta:
        model = ResourceFile
        fields = ("url", "path", "name", "doc", "doc_format", "keywords")
