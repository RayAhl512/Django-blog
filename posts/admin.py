from django.contrib import admin
from .models import BlogPost
from .models import Comment

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'post_author', 'post_created_date', 'post_updated_date')
    search_fields = ('post_title', 'post_content')
    list_filter = ('post_created_date', 'post_author')
    ordering = ('-post_created_date',) 

    readonly_fields = ('post_created_date', 'post_updated_date',)  # This line ensures these fields are non-editable, since i dont want people changing it after they make a post

    fieldsets = (
        ('Post Information', {
            'fields': ('post_title', 'post_content')
        }),
        ('Author and Date Information', {
            'fields': ('post_author', 'post_created_date', 'post_updated_date')
        }),
    )
      #field set is helping me make the blog more user friendly
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'content', 'created_date', 'updated_date')
    search_fields = ('content', 'author__username', 'post__post_title')
    list_filter = ('created_date', 'updated_date', 'author')
    ordering = ('-created_date',) 