from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('categories/<int:pk>',views.category_detail,name='category_detail'),
    path('subjects/<int:pk>',views.subject_detail,name='subject_detail'),
    path('subject2s/<int:pk>',views.subject2_detail,name='subject2_detail'),
    path('subject2s/new',views.subject2_create,name='subject2_create'),
    path('helps/',views.help_list,name='help_list'),
    path('helps/<int:pk>',views.help_detail,name='help_detail'),
    path('helps/new',views.help_create,name='help_create'),
]