from django.db import models
from datetime import datetime


class NewsPortal(models.Model):
    url = models.URLField(max_length = 200)
    html_tag = models.CharField(max_length = 25)
    class_name = models.CharField(max_length = 100)
    date = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.url

