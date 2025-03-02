from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username


class Reviews(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    review = models.TextField(default='None',max_length=999)
    rate = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    movie = models.CharField(default='Unknown', max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.review
    
