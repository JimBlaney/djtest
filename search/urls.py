from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('search', views.results_postback, name='search'),
  path('results/<str:search_term>', views.results, name='results'),
]