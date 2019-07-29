from django.urls import path, include
from website.views import index,sobre,cadastro,ideias

urlpatterns = [
    path('', index),
    path('sobre', sobre),
    path('cadastro', cadastro),
    path('ideias',ideias)
]