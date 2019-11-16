from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('category/', views.category_list, name='category_list'),
    path('categories/<int:pk>',views.category_detail,name='category_detail'),
    path('subjects/<int:pk>',views.subject_detail,name='subject_detail'),
    path('subject2s/<int:pk>',views.subject2_detail,name='subject2_detail'),
    path('subject2s/new',views.subject2_create,name='subject2_create'),
    path('subject2s/<int:pk>/delete',views.subject2_delete,name='subject2_delete'),
    path('helps/',views.help_list,name='help_list'),
    path('helps/<int:pk>',views.help_detail,name='help_detail'),
    path('helps/new',views.help_create,name='help_create'),
    path('subject2s/<int:pk>/edit',views.subject2_edit,name='subject2_edit'),
    path('helps/<int:pk>/edit',views.help_edit,name='help_edit'),
    path('helps/<int:pk>/delete',views.help_delete,name='help_delete'),
]