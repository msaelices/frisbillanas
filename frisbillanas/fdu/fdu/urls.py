from django.conf.urls import patterns, include, url
from django.contrib import admin

from landing import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    (r'^summernote/', include('django_summernote.urls')),
    # url(r'^blog/', include('blog.urls')),
    url(r'^rosetta/', include('rosetta.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
