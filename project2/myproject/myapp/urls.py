from django.test import TestCase
from django.urls import path
from .views import FacultyCreateView, FacultyListView, FacultyUpdateView, FacultyDeleteView

urlpatterns = [
    path('faculty/', FacultyListView.as_view(), name='faculty_list'),
    path('faculty/add/', FacultyCreateView.as_view(), name='faculty_add'),
    path('faculty/update/<int:pk>/', FacultyUpdateView.as_view(), name='faculty_update'),
    path('faculty/delete/<int:pk>/', FacultyDeleteView.as_view(), name='faculty_delete'),
]


# Create your tests here.
