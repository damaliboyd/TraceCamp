from django.shortcuts import render
from django.http import HttpResponse
from kickstarterapp.models import Kickstarter
from django.core import serializers

# Create your views here.
def kickstarter_view(request, kickstarter_id):
    kickstarter = Kickstarter.objects.filter(id = kickstarter_id)
    data = serializers.serialize("json", kickstarter)
    return HttpResponse(data)
