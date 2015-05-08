from django.conf.urls import patterns, include, url
from rest_framework import routers
from talos import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'libraries', views.LibraryFileViewSet)
router.register(r'resource_files', views.ResourceFileViewSet)
router.register(r'keywords', views.KeywordViewSet)
router.register(r'testcases', views.TestcaseViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
