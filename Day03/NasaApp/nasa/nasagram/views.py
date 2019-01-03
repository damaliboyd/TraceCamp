from django.shortcuts import render
from django.http import HttpResponse
from nasagram.models import Nasagram
from datetime import datetime
import requests
from django.shortcuts import redirect
# Create your views here.
def nasa_comment(request, id):
    nasa_com = Nasagram.objects.get(id=id)
    return render(request, 'nasa_comment.html/', {"nasa_com" : nasa_com})

def nasa_create(request):
    if (request.method == "GET"):
        date = request.GET.get("pick_date")
        api_key = "oMrH77hL0IcYFpEAYw6HpzxULiro2VX2jGy9CIMV"
        r = requests.get(f'https://api.nasa.gov/planetary/apod?date={date}&api_key={api_key}')
        url = r.json()["url"]

        return render(request, "nasa_create.html", {'picture': url, 'date':date})

    elif(request.method == "POST"):
        nasa_comment = Nasagram.objects.create(
            comment =  request.POST.get('comment', ""),
            date =  datetime.strptime(request.POST.get('date', '2018-01-01'), "%Y-%m-%d").date(),
            rating = request.POST.get('rating', 0),
            favorite =  request.POST.get('favorite', False) == "on",
            url =  request.POST.get('url', "")
        )
        return redirect(f'/nasa/comment/{nasa_comment.id}')

    else:
        return HttpResponse("Oh No! How did you get here?")





def nasa_list(request):
    nasa_com = Nasagram.objects.all()
    return render(request, "nasa_list.html", {'nasa_com' : nasa_com})

def nasa_date(request):
    return render(request, "nasa_date.html")
