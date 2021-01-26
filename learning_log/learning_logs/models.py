from django.db import models

# Create your models here.

class Topic(models.Model):
    "a topic which the user is learning about"
    text = models.CharField(max_length=200)
    date_added = models.DateTime(auto_now_add=True)


    def _str_(self):
        '''return string representation of model'''
        return self.text
