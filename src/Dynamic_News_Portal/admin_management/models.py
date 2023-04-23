from django.db import models
from datetime import datetime



CATAGORY_CHOICES = (("SP", "SPORTS"), ("ENT", "ENTERTAINMENT"), ("POL", "POLITICS"))


class NewsPortal(models.Model):
    portal_name = models.CharField(max_length = 100, null=True)
    url = models.URLField(max_length = 200)
    html_tag = models.CharField(max_length = 25)
    class_name = models.CharField(max_length = 100)
    date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.url


class TopNews(models.Model):
    created_date = models.DateTimeField(auto_now = True)
    catagory = models.CharField(choices = CATAGORY_CHOICES, max_length = 50)
    rank = models.IntegerField()
    text = models.TextField()


    def __str__(self):
        return self.catagory+"-"+str(self.rank)



