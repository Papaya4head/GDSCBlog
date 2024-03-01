from django.db import models

# Create your models here.
from django.db import models
from Blogapp.models import Post  

class comment(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=255)
    published_date = models.DateTimeField(auto_now_add=True)  
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  
