from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# Create your views here.
def home(request):
    return render(request, 'base.html',{})

def new_search(request):
    search = request.POST.get('search')
    response = requests.get(f'https://www.ebay-kleinanzeigen.de/s-berlin/{search}/k0l3331')
    data = response.text
    print(data)
    context = {
        'search': search
    }
    return render(request, 'my_app/new_search.html',context)