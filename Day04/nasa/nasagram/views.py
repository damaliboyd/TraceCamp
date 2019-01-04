from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, CreateView
from django.views.generic import  DetailView, DeleteView, UpdateView
from nasagram.forms.forms import NasaForm
from django import forms
import requests
from nasagram.models import nasagram

print(NasaForm)

# Create your views here.
class DateTemplateView(TemplateView):
    template_name = "date.html"

class CommentCreateView(CreateView):

    def __init__(self):
        super().__init__()
        self.image_url = " "

    form_class = NasaForm
    template_name = 'nasagram/comment_create_view.html'

    def get_initial(self, **kwargs):
        initial_form = super().get_initial(**kwargs)
        initial_form['date'] = self.date = self.request.GET.get("date_selector", "")
        initial_form['url'] = self.url = self.request.GET.get("url", "")

    def get(self,request):
        date = request.GET.get("pick_date")
        api_key = "oMrH77hL0IcYFpEAYw6HpzxULiro2VX2jGy9CIMV"
        r = requests.get(f'https://api.nasa.gov/planetary/apod?date={date}&api_key={api_key}')
        url = r.json()["url"]
        self.image_url = url
        get_response = super().get(request)
        return get_response


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["url"] = self.image_url
        return context

class CommentDetailView(DetailView):
    model = nasagram


class CommentDestroy(DeleteView):
    pass

class CommentUpdate(UpdateView):
    pass
