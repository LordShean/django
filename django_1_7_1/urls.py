from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_1_7_1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r"^polls/", include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
)