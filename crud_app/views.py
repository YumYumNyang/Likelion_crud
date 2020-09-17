from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from .models import Letter

# Create your views here.

class LetterListView(ListView):
    model = Letter
    template_name = "index.html"
    context_object_name = "letters"


class LetterDetailView(DetailView):
    model = Letter
    template_name="detail.html"
    context_object_name = "letter_object"

class LetterCreateView(CreateView):
    model = Letter
    template_name = "create.html"
    fields = '__all__'
    
    success_url= reverse_lazy('index')

class LetterDeleteView(DeleteView):
    model = Letter
    success_url =reverse_lazy('index')
    def get(self, *args,**kwargs):
        return self.post(*args,**kwargs)# get요청이 들어오면 바로 post 실행 post: 지워지는 기능하는 게 잇어!
        