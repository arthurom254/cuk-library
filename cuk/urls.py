from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('search',views.search,name="search"),
    path('units/<str:name>/', views.units,name='units'),
    path('read/<str:value>', views.papers,name='papers'),
    path('read/<str:value>/<str:id>', views.study,name='study'),
]