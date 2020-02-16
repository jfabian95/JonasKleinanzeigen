from django.shortcuts import render
from bs4 import BeautifulSoup
from .models import Search
import requests

# Create your views here.
def home(request):
    return render(request, 'base.html',{})

def new_search(request):
    search = request.POST.get('search')
    Search.objects.create(search=search)
    complete_search = search.replace(' ', '-')
    response = requests.get(f'https://www.ebay-kleinanzeigen.de/s-berlin/{complete_search}/k0')
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')

    post_articles = soup.find_all('article',{'class':'aditem'})

    postings = []

    for post in post_articles: 
        post_title          = post.find('a',{'class':'ellipsis'}).text
        post_url            = post.find('a',{'class':'ellipsis'}).get('href')
        post_description    = post.find('div',{'class':'aditem-main'}).p.text
        adimage = post.find('div',{'class':'is-nopic'})
        if adimage is None:
            post_picture    = post.find('div',{'class':'imagebox srpimagebox'}).get("data-imgsrc")
        else:
            post_picture    = ""
        post_price          = post.find('div',{'class':'aditem-details'}).strong.text

        postings.append((post_title, post_url, post_description, post_picture, post_price))
        print(post_url)
    context = {
        'search': search,
        'postings':postings
    }
    return render(request, 'my_app/new_search.html',context)