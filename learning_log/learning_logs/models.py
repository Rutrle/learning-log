from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    "a topic which the user is learning about"
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True) #sets the attribute to time when user will add a date
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        '''return string representation of model'''
        return self.text

class Entry(models.Model):
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE)
    text=models.TextField()
    date_added = models.DateTimeField(auto_now_add=True) #sets the attribute to time when user will add a date

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        if len(self.text)>50:
            entry_str = f"{self.text[:50]}..."
        else:
            entry_str = f"{self.text[:50]}"   
        return entry_str
