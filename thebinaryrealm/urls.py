from django.conf.urls import patterns, include, url
from thebinaryrealm import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
	'',
    url(r'^$', 'blog.views.index'),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

# Serving static files
urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
