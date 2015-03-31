from django.conf.urls import patterns, include, url
from rest_framework import routers
from talos import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'collections', views.CollectionViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

old_urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'talos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
