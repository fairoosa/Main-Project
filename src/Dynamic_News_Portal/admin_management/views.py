from django.shortcuts import render
from django.views import generic
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy

class HomePage(generic.TemplateView):
    template_name = "home.html"

    def post(self, request, *args, **kwagrs):
        news_portal = self.request.POST['np']
        duration = self.request.POST['du']
        print(news_portal,duration)
        return redirect(reverse_lazy("home"))


