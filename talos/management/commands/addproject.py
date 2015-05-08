from talos import models
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
import sys, os.path
from talos.parser import RobotFile
import re

class Command(BaseCommand):
    '''Add the resource files and suites within a folder'''
    args = "<pathname pathname ...>"
    help = "Add a project to the talos database"

    def handle(self, *args, **kwargs):
        if len(args) == 0:
            raise CommandError("usage: addproject path")

        for path in args:
            project_abspath = os.path.abspath(os.path.expanduser(path))
            sys.stdout.write("adding %s...\n" % project_abspath)
            (project, created) = models.Project.objects.get_or_create(root=project_abspath)
            if created:
                project.save()

            for root, dirs, files in os.walk(project_abspath):
                for filename in files:
                    fullpath = os.path.join(root, filename)
                    ext = filename.rsplit(".", 1)[-1].lower()

                    # FIXME: need to support tsv at some point...
                    if ext in ("robot", "txt"):
                        robot_file = RobotFile.factory(fullpath)
                        if robot_file is None:
                            # not a robot file (eg: __init__.robot)
                            continue

                        # FIXME: need to add support for library files (.py and .xml ...)
                        if robot_file.type == "resource":
                            collection, created = models.ResourceFile.objects.get_or_create(path=fullpath)

                        elif robot_file.type == "suite":
                            collection, created = models.SuiteFile.objects.get_or_create(path=fullpath)

                        if not created:
                            # out with the old, in with the new!
                            collection.keywords.all().delete()
                            
                        collection.name = robot_file.name
                        collection.doc = robot_file.settings.get("documentation", "")
                        collection.save()
                        
                        with transaction.atomic():
                            for keyword in robot_file.keywords:
                                doc = "\n".join(keyword.get_setting("documentation", []))
                                args = ", ".join(keyword.get_setting("arguments"))
                                kw, created = collection.keywords.get_or_create(name=keyword.name, doc=doc, args=args)
                                kw.save()
