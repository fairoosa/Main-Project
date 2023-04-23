from django.shortcuts import render
from django.views import generic
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from bs4 import BeautifulSoup
import requests
from .models import NewsPortal, TopNews


class HomePage(generic.TemplateView):
    template_name = "home.html"

    

    def post(self, request, *args, **kwagrs):
        url = self.request.POST['np'].strip()
        html_tag = self.request.POST['tag'].strip()
        class_name = self.request.POST['class'].strip()

        NewsPortal.objects.create(url=url, html_tag=html_tag, class_name=class_name)
        print("news poratl: ", url, "html_tag: ", html_tag, "class_name: ", class_name)

        return redirect(reverse_lazy("home"))



class TrendingNews(generic.ListView):
    template_name = "news.html"
    model = TopNews
    






    



