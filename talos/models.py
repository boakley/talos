from django.db import models


# The more I think about it, the more useless this class becomes.
# Does this app really need to track projects?
class Project(models.Model):
    root = models.CharField(max_length=2048, unique=True, null=False)

    def __unicode__(self):
        return self.root

class Collection(models.Model):
    '''
    A collection of keywords (eg: a resource file or library)
    '''

    path = models.CharField(max_length=2048, null=False, unique=True)
    name = models.CharField(max_length=256)
    collection_type = models.CharField(max_length=8, 
                                       choices=(
                                           ("library", "Library"), 
                                           ("resource", "Resource file"),
                                           ("suite", "Test suite"),
                                       ),
    )
    doc = models.TextField(blank=True)
    doc_format = models.CharField(max_length=10, 
                                  choices=(("HTML", "HTML"),
                                           ("TEXT", "Plain text"),
                                           ("ROBOT", "Robot"),
                                           ("reST", "reStructured Text")),
                                  default="ROBOT")

    # these three only apply to libraries, not resource files
    # or test suites. Should I use a separate model for libraries,
    # resource files and so on? I guess this is good enough for now.
    version = models.CharField(max_length=12, blank=True)
    scope = models.CharField(max_length=6, 
                             choices=(("global", "Global"),
                                      ("suite", "Test suite"),
                                      ("test", "Test case"),
                                      ("", "none")),
                             default="global")
    namedargs = models.CharField(blank=True, max_length=2048)

    def keywords(self):
        return Keyword.objects.filter(collection=self)

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



