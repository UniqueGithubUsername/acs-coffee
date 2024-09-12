from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('export/', views.export, name='export'),
    path('broadcast/', views.broadcast, name='broadcast'),
    path('importxlsx/', views.importxlsx, name='importxlsx'),
    path('add/<int:id>', views.add, name='add'),
]