from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('export/', views.export, name='export'),
    path('calcdebth/', views.calcdebth, name='calcdebth'),
    path('broadcast/', views.broadcast, name='broadcast'),
    path('importxlsx/', views.importxlsx, name='importxlsx'),
    path('user/<slug:slug>', views.user, name='user'),
    path('mail/<int:id>', views.mailtoemployee, name='mail'),
    path('getlink/<int:id>', views.getlink, name='getlink'),
    path('add/<slug:slug>', views.add, name='add'),
    path('newemployee/', views.newemployee, name='newemployee'),
    path('faq/', views.faq, name='faq')
]