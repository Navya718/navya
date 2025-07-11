from django.shortcuts import render

from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Book

class studentkCreateView(CreateView):
    model = student
    fields = ['title', 'author', 'publication_date']
    template_name = 'student_form.html'  # Optional: specify custom template
    success_url = reverse_lazy('book_list')  # URL to redirect to after successful form submission

class studentListView(ListView):
    model = student
    context_object_name = 'student'  # Optional: specify the context variable name in templates
    template_name = 'student_list.html'  # Optional: specify custom template

class studentUpdateView(UpdateView):
    model = student
    fields = ['title', 'author', 'publication_date']
    template_name = 'student_form.html'  # Optional: specify custom template
    success_url = reverse_lazy('student_list')  # URL to redirect to after successful form submission

class studentDeleteView(DeleteView):
    model = student
    template_name = 'student_confirm_delete.html'  # Optional: specify custom template
    success_url = reverse_lazy('book_list')  # URL to redirect to after successful deletion


# Create your views here.
