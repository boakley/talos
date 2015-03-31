from django.db import models


# I don't remember where I was going with the ProjectManager class...
# 
# class ProjectManager(models.Manager):
#     '''
#     '''
#     def create_project(self, path):
#         project = self.create(root=path)

#         # <this is where we would populate the db>

#         return project

# Create your models here.
class Project(models.Model):
    root = models.CharField(max_length=1024)
#    objects = ProjectManager()

    def __unicode__(self):
        return self.root

class Collection(models.Model):
    '''
    A collection of keywords (eg: a resource file or library)
    '''
    project = models.ForeignKey(Project, null=True)
    path = models.CharField(max_length=2048, null=True)
    name = models.CharField(max_length=256)
    collection_type = models.CharField(max_length=8, 
                                       choices=(
                                           ("library", "Library"), 
                                           ("resource", "Resource file"),
                                           ("suite", "Test suite"),
                                       ),
    )
    version = models.CharField(max_length=12, blank=True)
    scope = models.CharField(max_length=6, 
                             choices=(("global", "Global"),
                                      ("suite", "Test suite"),
                                      ("test", "Test case")),
                             default="global")
    namedargs = models.CharField(blank=True, max_length=2048)
    doc_format = models.CharField(max_length=10, 
                                  choices=(("HTML", "HTML"),
                                           ("TEXT", "Plain text"),
                                           ("ROBOT", "Robot"),
                                           ("reST", "reStructured Text")),
                                  default="ROBOT")
    doc = models.TextField(blank=True)

    def __unicode__(self):
        if self.path is None:
            return unicode(self.name)
        else:
            return unicode(self.path)

class Testcase(models.Model):
    collection = models.ForeignKey(Collection)
    name = models.CharField(max_length=256) # what is the actual robot limit?
    doc = models.TextField("Documentation", blank=True)
    
class Keyword(models.Model):
    collection = models.ForeignKey(Collection)
    name = models.CharField(max_length=256) # what is the actual robot limit?
    args = models.CharField(max_length=256) 
    doc = models.TextField("Documentation", blank=True)

    def __unicode__(self):
        return self.name



