from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=60, blank=False)
    description = models.CharField(max_length=240)
    content = models.TextField(blank=False)

    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title