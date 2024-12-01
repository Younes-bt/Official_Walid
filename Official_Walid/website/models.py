from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField
User = get_user_model()

# Create your models here.



class Article(models.Model):
    title = models.CharField(max_length=500, null=False, blank=False)
    imgUrl = CloudinaryField('image', blank=True, null=True)
    content = models.TextField(null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} by {self.author.username}'
    
class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_authors")
    content = models.TextField(null=False, blank=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now=True)