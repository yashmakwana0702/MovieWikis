from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import requests



def index(request):
    return render(request,"home.html")


def searchresult(request):
    query= "avenger"
    url= 'https://imdb-api.com/en/API/SearchMovie/k_pftzqnp0/'+ query
    print(url)
    movie_data=requests.get(url).json
    context={'movie_data': movie_data}
    return render(request,'result.html',context)    