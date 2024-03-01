from django.db import models

# Create your models here.
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)  
    content = models.TextField()
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='posts/')  
    tags = models.CharField(max_length=255)  
    created_at = models.DateTimeField(auto_now_add=True)
