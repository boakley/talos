from django.db import models

# see http://stackoverflow.com/questions/20895429/how-exactly-do-django-content-types-work
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey

# don't allow objects with names longer than this. I'm too lazy to look
# up the actual maximum imposed by robot...
MAX_NAME_LENGTH=256

# The more I think about it, the more useless this class becomes.
# Does this app really need to track projects? If the answer is
# "yes", we probably need to add a reference to child objects
class Project(models.Model):
    root = models.CharField(max_length=2048, unique=True, null=False)

    def __unicode__(self):
        return self.root

class ResourceFile(models.Model):
    name = models.CharField(max_length=MAX_NAME_LENGTH)
    path = models.CharField(max_length=2048, null=False, unique=True)
    doc = models.TextField(blank=True)
    doc_format = models.CharField(max_length=10, 
                                  choices=(("HTML", "HTML"),
                                           ("TEXT", "Plain text"),
                                           ("ROBOT", "Robot"),
                                           ("reST", "reStructured Text")),
                                  default="ROBOT")
    keywords = GenericRelation('Keyword')

    def __unicode__(self):
        if self.path is None:
            return unicode(self.name)
        else:
            return unicode(self.path)

class SuiteFile(models.Model):
    name = models.CharField(max_length=MAX_NAME_LENGTH)
    path = models.CharField(max_length=2048, null=False, unique=True)
    doc = models.TextField(blank=True)
    doc_format = models.CharField(max_length=10, 
                                  choices=(("HTML", "HTML"),
                                           ("TEXT", "Plain text"),
                                           ("ROBOT", "Robot"),
                                           ("reST", "reStructured Text")),
                                  default="ROBOT")

    keywords = GenericRelation('Keyword')

    def testcases(self):
        return Testcase.objects.filter(parent=self)

    def __unicode__(self):
        if self.path is None:
            return unicode(self.name)
        else:
            return unicode(self.path)


class LibraryFile(models.Model):
    name = models.CharField(max_length=MAX_NAME_LENGTH)
    path = models.CharField(max_length=2048, null=False, unique=True)
    doc = models.TextField(blank=True)
    doc_format = models.CharField(max_length=10, 
                                  choices=(("HTML", "HTML"),
                                           ("TEXT", "Plain text"),
                                           ("ROBOT", "Robot"),
                                           ("reST", "reStructured Text")),
                                  default="ROBOT")

    version = models.CharField(max_length=12, blank=True)
    scope = models.CharField(max_length=6, 
                             choices=(("global", "Global"),
                                      ("suite", "Test suite"),
                                      ("test", "Test case"),
                                      ("", "none")),
                             default="global")
    namedargs = models.CharField(blank=True, max_length=2048)

    keywords = GenericRelation('Keyword')

    def __unicode__(self):
        if self.path is None:
            return unicode(self.name)
        else:
            return unicode(self.path)


class Testcase(models.Model):
    parent = models.ForeignKey(SuiteFile)
    name = models.CharField(max_length=MAX_NAME_LENGTH)
    doc = models.TextField("Documentation", blank=True)

    def __unicode__(self):
        return self.name
    
class Keyword(models.Model):
    name = models.CharField(max_length=MAX_NAME_LENGTH)
    doc = models.TextField("Documentation", blank=True)
    args = models.CharField(max_length=256) 

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return self.name

