from django.shortcuts import render
from django.views import generic
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from bs4 import BeautifulSoup
import requests
from .models import NewsPortal, TopNews
from django.shortcuts import render
from newsapi import NewsApiClient
from elasticsearch import Elasticsearch, helpers


es = Elasticsearch(['http://localhost:9200'])


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
    template_name = "index copy.html"
    model = TopNews
    
    def get_context_data(self, **kwargs):
        category = self.request.GET.get("category")
        data = super().get_context_data(**kwargs)
        data['page_title'] = 'Authors'
        data['news'] = es.search(index="indian-news", body={"query":{"match_all":{}}})
        if not category:
            data['news_world'] = es.search(index="sports-news", body={"query":{"match_all":{}}})
        else:
            index = f'{category}-news'
            data['news_world'] = es.search(index=index, body={"query":{"match_all":{}}})
             
        
        news_list = []
        for i in data['news']['hits']['hits']:
            dict_ = {
                 "name": i['_source']['name'],
                 "title": i['_source']['title'],
                 "desc": i['_source']['description'],
                 "image": i['_source']['image'],
                 "content": i['_source']['content'],
                 "url": i['_source']['url'],
			}
            news_list.append(dict_)
        data['news'] = news_list

        inter_news_list = []
        for i in data['news_world']['hits']['hits']:
            dict_ = {
                 "name": i['_source']['name'],
                 "title": i['_source']['title'],
                 "desc": i['_source']['description'],
                 "image": i['_source']['image'],
                 "content": i['_source']['content'],
                 "url": i['_source']['url'],
			}
            inter_news_list.append(dict_)
        data['news_world'] = inter_news_list
        return data
 


# importing api



# Create your views here.
def index(request):
	
	newsapi = NewsApiClient(api_key ='YOURAPIKEY')
	top = newsapi.get_top_headlines(sources ='techcrunch')

	l = top['articles']
	desc =[]
	news =[ "uhdvdju hususbjb csjgjjsh vudksnn fairoosa ihisfus jgjisgsvcs"]
	img =[]

	for i in range(len(l)):
		f = l[i]
		news.append(f['title'])
		desc.append(f['description'])
		img.append(f['urlToImage'])
	mylist = zip(news, desc, img)

	return render(request, 'index.html', context ={"mylist":mylist})

    






    



