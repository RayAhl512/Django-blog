from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Comment
from django.http import HttpResponseRedirect
from django.urls import reverse


def post_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, pk):
    # Using get_object_or_404 for safety
    post = get_object_or_404(BlogPost, pk=pk)

    # Check if the request is a POST (i.e., a form submission)
    if request.method == "POST":
        # Get content from the form (the comment submitted by a user)
        content = request.POST.get('content')

        # Create a new comment object and save to the database
        comment = Comment(post=post, author=request.user, content=content)
        comment.save()

        # Redirect to the same page after saving the comment
        return HttpResponseRedirect(reverse('post_detail', args=(post.id,)))

    # Fetch all comments associated with the post
    comments = post.comments.all()

    # If the request is a GET, display the post details and comments
    return render(request, 'post_detail.html', {'post': post, 'comments': comments})
