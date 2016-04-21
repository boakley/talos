from rest_framework import serializers
from talos.models import Project, LibraryFile, ResourceFile, Testcase, Keyword, SuiteFile
from generic_relations.relations import GenericRelatedField

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ("root",)


class TestcaseSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="testcase-detail")
    parent = serializers.HyperlinkedRelatedField(view_name="suitefile-detail", read_only=True)
    class Meta:
        model = Testcase
        fields = ("url", "name", "parent")


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


class KeywordSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name="keyword-detail")
    # see https://github.com/Ian-Foote/rest-framework-generic-relations
    parent = GenericRelatedField({
        ResourceFile: serializers.HyperlinkedRelatedField(
            queryset= ResourceFile.objects.all(),
            view_name="resourcefile-detail"
        ),
        SuiteFile: serializers.HyperlinkedRelatedField(
            queryset= SuiteFile.objects.all(),
            view_name="suitefile-detail"
        ),
        LibraryFile: serializers.HyperlinkedRelatedField(
            queryset= LibraryFile.objects.all(),
            view_name="libraryfile-detail"
        ),
    })

    class Meta:
        model = Keyword
        fields = ("url", "name", "doc", "args", "parent")

