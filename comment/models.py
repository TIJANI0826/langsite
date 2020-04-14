from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from blog.models import Post

# Create your models here.
class Comment(models.Model):
    post  =  models.ForeignKey(Post,on_delete = models.CASCADE, related_name="comments",default=1)
    # post =  models.ForeignKey(Post,on_delete = models.CASCADE)
    # Generic foreign keys
    name  = models.CharField(max_length=80, default='user')
    email = models.EmailField(default="none")
    body = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
    
    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

