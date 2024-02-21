from django.db import models

# Create your models here.
class book(models.Model):
    Name=models.CharField(max_length=50)
    picture=models.ImageField()
    author=models.CharField(max_length=30 ,default='Author')
    Email=models.EmailField(blank=True)
    Description=models.TextField(default='Book Discription')

    def __str__(self):
        return self.Name

