from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'blog.views.index', name='index_url'),
    url(r'(?P<slug>[\w\-]+)/$', 'blog.views.post', name='post_url')
)
