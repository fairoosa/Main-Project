from django.shortcuts import render
from django.views import generic
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from bs4 import BeautifulSoup
import requests

class HomePage(generic.TemplateView):
    template_name = "home.html"

    def post(self, request, *args, **kwagrs):
        url = self.request.POST['np']
        duration = self.request.POST['du'] 

        print("news poratl: ", url, "duration: ", duration)

        response = requests.get(url)
        print("response: ", response)

        html_content = response.content
        print("html content: ", html_content)

        soup = BeautifulSoup(html_content, "html.parser") 
        print("SOUP: ", soup)
        
        title1 = soup.find('h1', class_='title').text
        print('Title:', title1)

        title2 = soup.find('h3', class_='sub-title').text
        print('Sub-Title:',title2)

        contents = soup.find('div', id='content-body-65035597').text
        print('Content :', contents)
        return redirect(reverse_lazy("home"))
