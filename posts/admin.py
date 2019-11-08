from django.contrib import admin
from .models import Post,Comment
from django_summernote.admin import SummernoteModelAdmin

class CommentInline(admin.StackedInline):
    model = Comment

class PostAdmin(SummernoteModelAdmin):
    inlines = [CommentInline, ]
    summernote_fields = ('desc',)

admin.site.register(Post, PostAdmin)


