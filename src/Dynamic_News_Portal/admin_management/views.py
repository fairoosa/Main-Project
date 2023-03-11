from django.shortcuts import render
from django.views import generic
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from bs4 import BeautifulSoup
import requests
from .models import NewsPortal


class HomePage(generic.TemplateView):
    template_name = "home.html"

    def post(self, request, *args, **kwagrs):
        url = self.request.POST['np'].strip()
        html_tag = self.request.POST['tag'].strip()
        class_name = self.request.POST['class'].strip()

        NewsPortal.objects.create(url=url, html_tag=html_tag, class_name=class_name)
        print("news poratl: ", url, "html_tag: ", html_tag, "class_name: ", class_name)

        # response = requests.get(url)
        # # print("response: ", response)

        # html_content = response.content
        # # print("html content: ", html_content)

        # soup = BeautifulSoup(html_content, "html.parser") 
        # # print("SOUP: ", soup)
        
        # title1 = soup.find(html_tag, class_ = class_name).text
        # print('Title:', title1)

        # # title2 = soup.find('h3').text
        # # print('Sub-Title:',title2)


        # contents = soup.find('div', id='content-body-65035597').text
        # print('Content :', contents)
        return redirect(reverse_lazy("home"))
