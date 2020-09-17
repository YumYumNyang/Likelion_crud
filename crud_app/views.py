from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Letter
# Create your views here.

class LetterListView(ListView):
    model = Letter
    template_name = "index.html"
    context_object_name = "letters"