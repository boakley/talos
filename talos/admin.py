from django.contrib import admin
from talos.models import (Project, 
                          ResourceFile, LibraryFile, SuiteFile, 
                          Keyword, Testcase)

class ResourceFileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['path', 'name']}),
        ("Documentation", {'fields': ['doc_format', 'doc']}),
    ]
    list_display = ('name', 'path')
    search_fields = ['path']

class LibraryFileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['path', 'name']}),
        ("Documentation", {'fields': ['doc_format', 'doc']}),
        ("Library Information", {'fields': ['version', 'scope', 'namedargs']})
    ]
    list_display = ('name', 'path')
    search_fields = ['path']

class SuiteFileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'path', 'doc']}),
    ]
    list_display = ('name', 'path')
    search_fields = ['path']

admin.site.register(Project)
admin.site.register(ResourceFile, ResourceFileAdmin)
admin.site.register(LibraryFile, LibraryFileAdmin)
admin.site.register(SuiteFile, SuiteFileAdmin)
admin.site.register(Keyword)
admin.site.register(Testcase)

