from django.shortcuts import render
from animalapp import models
from django.views.generic import TemplateView, CreateView, ListView,UpdateView, DeleteView


# Create your views here.


class AnimalHomeView(TemplateView):
    pass
class AnimalCreateView(CreateView):
    pass
class AnimalReadView(ListView):
    pass
class AnimalUpdateView(UpdateView):
    pass
class AnimalDeleteView(DeleteView):
    pass


