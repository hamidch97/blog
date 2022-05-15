from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Profil(models.Model):
    user = models.OneToOneField(User , null=True , on_delete=models.CASCADE)
    bio = models.TextField()
    profil_pic = models.ImageField(null = True , blank = True , upload_to="img/profile")
    website_url = models.CharField(max_length=255,null=True , blank=True)
    facebook_url = models.CharField(max_length=255,null=True , blank=True)
    instagram_url= models.CharField(max_length=255,null=True , blank=True)
    

    def __str__(self) -> str:
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_imag = models.ImageField(null = True , blank = True , upload_to="img/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #body = models.TextField()
    body = RichTextField(blank=True,null=True)
    date_post = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default="coding")
    snippet = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='blog_post')

    def total_likes(self):
        return self.likes.count()
    
    def __str__(self) -> str:
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

class Coment(models.Model):
    post = models.ForeignKey(Post,related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.post.title}-{self.name}"