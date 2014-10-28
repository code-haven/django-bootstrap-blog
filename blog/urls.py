from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'blog.views.index', name='index_url'),
    url(r'^hello-world$', 'blog.views.post', name='post_urk')
)
