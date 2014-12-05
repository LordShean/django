from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_1_7_1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #adding the name space
    #it's possible having the same url name thought in many app
    #ex polls:index VS whatever:index
    url(r"^polls/", include('polls.urls', namespace='polls')),
    url(r'^admin/', include(admin.site.urls)),
)