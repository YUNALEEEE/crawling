from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
# Create your views here.

def home(request):
    if request.method=="POST":
        keyword = request.POST.get('keyword')

        URL = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query="
        fullURL = URL+keyword
        data = requests.get(fullURL).text

        soup = BeautifulSoup(data, 'html.parser')
        news_titles = soup.find_all(class_='_sp_each_title')
        title_list=[]
        for title in news_titles:
            title_list.append({'url': title.get('href'), 'title': title.get('title')})
        return render(request, 'result.html', {'title_list': title_list})

    else:
        return render(request, 'home.html')

def result(request):
    return render(request, 'result.html')