from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dog

# Define the home view


def home(request):
    return HttpResponse('<h1>Hey</h1>')


def about(request):
    return render(request, 'about.html')


def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {'dogs': dogs})


def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    return render(request, 'dogs/detail.html', {'dog': dog})


class DogCreate(CreateView):
    model = Dog
    fields = '__all__'
    success_url = '/dogs/'


class DogUpdate(UpdateView):
  model = Dog
  fields = ['description', 'age']


class DogDelete(DeleteView):
  model = Dog
  success_url = '/dogs/'
