from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    # The title of the blog post
    post_title = models.CharField(max_length=200)
    
    # The main content of the blog post
    post_content = models.TextField()
    
    # The author of the blog post (the person who wrote it)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # The date when the blog post was created
    post_created_date = models.DateTimeField(auto_now_add=True)
    
    # The date when the blog post was last updated
    post_updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        # A human-readable representation of the blog post (its title)
        return self.post_title  

class Comment(models.Model):
    # The blog post that this comment is attached to
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    
    # The person who wrote the comment
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # The content of the comment itself
    content = models.TextField()
    
    # The date when the comment was added
    created_date = models.DateTimeField(auto_now_add=True)
    
    # The date when the comment was last updated
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        # A friendly representation of the comment, mentioning the author and post
        return f"Comment by {self.author} on {self.post}"