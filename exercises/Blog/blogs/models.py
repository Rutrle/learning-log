from django.db import models

# Create your models here.

class Blogpost(models.Model):
    '''model for blogpost'''
    title = models.CharField(max_length=200)
    text = models.TextField()
    date =models.DateTimeField()