from django.test import TestCase
from django.urls import path
from .views import studentCreateView, studentListView 
from .views import studentUpdateView, studentDeleteView
urlpatterns = [
    path('', studentListView.as_view(), name='student_list'),
    path('create/', studentCreateView.as_view(), name='student_create'),
    path('update/<int:pk>/', studentUpdateView.as_view(), name='student_update'),
    path('delete/<int:pk>/', studentDeleteView.as_view(), name='student_delete'),
]


# Create your tests here.
