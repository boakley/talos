from django.test import TestCase
from talos.models import ResourceFile, Keyword

# Create your tests here.
class ResourceFileTests(TestCase):
    def setUp(self):
        self.resourceFile = ResourceFile(name="resource file", path="rf1.robot")
        self.resourceFile.save()
        
    def test_can_create_keyword(self):
        kw1 = Keyword(name="kw1", doc="kw1 doc...", parent=self.resourceFile)
        keywords = self.resourceFile.keywords.all()
        assert(len(keywords) > 0)
