from django.shortcuts import render
from .models import BlogPost

def post_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = BlogPost.objects.get(pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})
