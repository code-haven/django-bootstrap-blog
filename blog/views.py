from django.shortcuts import render
from blog.models import BlogPost


def index(request):
    latest_posts = BlogPost.objects.all()
    return render(request, 'blog/index.html', {'posts': latest_posts})


def post(request):
    blog_post = BlogPost.objects.get(slug='hello-world')
    return render(request, 'blog/post.html', {'post': blog_post})
