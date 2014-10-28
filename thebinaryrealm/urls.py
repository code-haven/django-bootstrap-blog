from django.conf.urls import patterns, include, url
from thebinaryrealm import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
	'',
    url(r'^$', 'blog.views.index'),
    url(r'^blog/', include('blog.urls')),

    url(r'^about/', 'thebinaryrealm.views.about'),
    url(r'^projects/', 'thebinaryrealm.views.projects'),
    url(r'^contact/', 'thebinaryrealm.views.contact'),
    
    url(r'^admin/', include(admin.site.urls)),

)

