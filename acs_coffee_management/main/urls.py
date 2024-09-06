from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('export/', views.export, name='export'),
    path('broadcast/', views.broadcast, name='broadcast')
]