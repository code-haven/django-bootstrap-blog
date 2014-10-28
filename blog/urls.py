from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    url(r'^$', 'blog.views.index', name='index_url'),
    url(r'(?P<slug>[\w\-]+)/$', 'blog.views.post', name='post_url'),
    url(r'^markdown/', include('django_markdown.urls')),
)
