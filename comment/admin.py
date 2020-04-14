from django.contrib import admin
from .models import Comment
from blog.models import Post
# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','body','post','created_on')
    list_filter = ('active', 'created_on')
    fields = ('name','email','body')
    actions = ['approve_comments']

    def approve_comments(self,request,queryset):
        return queryset.update(active=True)

admin.site.register(Comment)