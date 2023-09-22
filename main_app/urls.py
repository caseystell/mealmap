from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('recipes/', views.recipes_index, name='index'),
  path('recipes/create/', views.RecipeCreate.as_view(), name='recipes_create'),
  path('recipes/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipes_update'),
  path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipes_delete'),
  path('recipes/<int:recipe_id>/add_to_calendar/<int:date_id>/', views.add_to_calendar, name='add_to_calendar'),
  path('recipes/<int:recipe_id>/remove_from_calendar/<int:date_id>/', views.remove_from_calendar, name='remove_from_calendar'),
]