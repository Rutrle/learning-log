from django.db import models

# Create your models here.

class Blogpost(models.Model):
    '''model for blogpost'''
    title = models.CharField(max_length=200,unique=True)
    text = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title