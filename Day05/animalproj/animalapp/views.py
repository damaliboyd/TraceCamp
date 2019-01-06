from django.shortcuts import render
from animalapp import models
import requests
from animalapp.models import Animal, Image
from django.http import HttpResponse
from animalapp.forms.forms import AnimalForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView,UpdateView, DeleteView


# Create your views here.


class AnimalHomeView(TemplateView):
    template_name = "index.html"
class AnimalCreateView(UpdateView):
    model = Animal
    form_class = AnimalForm
    # Get request for animal
    # Using Petfinder API
    # https://www.petfinder.com/developers/api-docs
    # http://api.petfinder.com/my.method?key=12345&arg1=foo
    def get(self, request):
        api_key= "31b8ef47be5499bd9c27bbc4be9068fc"
        animal_type = self.request.GET.get("animal_type", "cat")
        animal_zip = self.request.GET.get("zip_code", "29440")
        r = requests.get(f'http://api.petfinder.com/pet.getRandom?key={api_key}&animal={animal_type}&output=basic&location={animal_zip}&format=json')
        pet_info = r.json()

        name = pet_info['petfinder']['pet']['name']['$t']
        age = pet_info['petfinder']['pet']['age']['$t']
        type_of = pet_info['petfinder']['pet']['animal']['$t']
        age = pet_info['petfinder']['pet']['age']['$t']
        images = pet_info['petfinder']['pet']['media']['photos']['photo']
        description = pet_info['petfinder']['pet']['description']
        zip = pet_info['petfinder']['pet']['contact']['zip']['$t']

        # Query for the animal based on fields to see if it already exists
        # Use .filter len(Animal.objects.filter(name = )) == 0
        if( len(Animal.objects.filter(name=name, age=age, description=description )) == 0):
            # Create stuff if it doesn't exist
            a_animal = Animal.objects.create (
                name = name,
                age = age,
                type_of = type_of,
                description = description,
                location = zip,
                liked = False
            )

            for img in images:
                if (img['$t'].find('width=300')) != -1:

                    Image.objects.create(
                        url = img['$t'],
                        animal = a_animal
                    )
        self.animal = a_animal


        return super().get(request)

    def post(self, request, *args, **kwargss):
        was_liked = request.POST.get('liked',FALSE) == 'on'
        Animal.objects.last().like = was_liked

    def get_object(self):
        return self.animal

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['animal'] = self.animal
        return context

class AnimalListView(ListView):
    model = Animal

class AnimalDeleteView(DeleteView):
    model = Animal
    success_url = reverse_lazy('animal_list')
