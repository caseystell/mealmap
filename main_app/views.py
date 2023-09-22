import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Recipe, Calendar
from .forms import MealForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def recipes_index(request):
    # recipes = Recipe.objects.filter(user=request.user)
    return render(request, 'recipes/index.html', 
    #     {'recipes': recipes}
    )

class RecipeCreate(CreateView):
  model = Recipe
  fields = ['title', 'url']

class RecipeUpdate(UpdateView):
  model = Recipe
  fields = ['title', 'url']

class RecipeDelete(DeleteView):
  model = Recipe
  success_url = '/recipes'

def add_meal(request, recipe_id):
  form = MealForm(request.POST)
  # validate the form
  if form.is_valid():
    new_meal = form.save(commit=False)
    new_meal.recipe_id = recipe_id
    new_meal.save()
  return redirect('index', recipe_id=recipe_id)

def add_to_calendar(request, recipe_id, date_id):
   Recipe.objects.get(id=recipe_id).calendar.add(date_id)
   return redirect('index', recipe_id=recipe_id)


def remove_from_calendar(request, recipe_id, date_id):
   Recipe.objects.get(id=recipe_id).calendar.remove(date_id)
   return redirect('index', recipe_id=recipe_id)