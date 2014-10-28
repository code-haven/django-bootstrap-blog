from django.shortcuts import render
from blog.models import BlogPost


def index(request):
    latest_posts = BlogPost.objects.all()
    return render(request, 'blog/index.html', {'posts': latest_posts})


def post(request, slug):
    blog_post = BlogPost.objects.get(slug=slug)
    return render(request, 'blog/post.html', {'post': blog_post})
