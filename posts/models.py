from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    post_title = models.CharField(max_length=200)
    post_content = models.TextField()
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_created_date = models.DateTimeField(auto_now_add=True)
    post_updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post_title