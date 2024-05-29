"""
URL configuration for MoviesList project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index,name='home'),
path("submit_form", views.submit_form,name='submit_form'),
path("add_movies", views.add_movies,name='add_movies'),
path("movies", views.movie_list,name='movie_list'),
path("filter_movies", views.filter_movies,name='filter_movies'),
path("search_movie_by_language", views.search_movie_by_language,name='search_movie_by_language'),
path("get_movie_counts", views.get_movie_counts,name='get_movie_counts'),
path('update_movie', views.update_movie, name='update_movie'),
path('delete_movie', views.delete_movie, name='delete_movie'),
]
