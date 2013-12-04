from django.conf.urls import patterns, include, url
from question import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.main, name='main'),
    # url(r'^((?P<my_int>\d+)/$)', views.answer, name='answer'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
