from django_markdown.admin import MarkdownModelAdmin
from django.contrib import admin
from blog.models import BlogPost

class BlogPostAdmin(MarkdownModelAdmin):
	list_display = ('title', 'created_at')
	prepopulated_fields = {'slug': ('title', )}

admin.site.register(BlogPost, BlogPostAdmin)