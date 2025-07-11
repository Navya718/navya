from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Faculty

class FacultyCreateView(CreateView):
    model = Faculty
    fields = ['name', 'age', 'qualification']
    template_name = 'faculty_form.html'
    success_url = reverse_lazy('faculty_list')

class FacultyListView(ListView):
    model = Faculty
    context_object_name = 'faculties'
    template_name = 'faculty_list.html'

class FacultyUpdateView(UpdateView):
    model = Faculty
    fields = ['name', 'age', 'qualification']
    template_name = 'faculty_form.html'
    success_url = reverse_lazy('faculty_list')

class FacultyDeleteView(DeleteView):
    model = Faculty
    template_name = 'faculty_confirm_delete.html'
    success_url = reverse_lazy('faculty_list')
2. master.html – No Change Needed
Your master.html can be reused for both Book and Faculty views:

html
Copy
Edit
<!-- templates/master.html -->
<html>
<head><title>
{% block title %}{% endblock %}
</title></head>
<body bgcolor="goldenrod"> 
    <h1 align="center">Welcome to Our College</h1>
    {% block content %}{% endblock %}
    <p>Author: Praveen Choudhary</p>
    <p>praveen.nsic@gmail.com</p>
</body>
</html>
3. Templates for Faculty Views
Create these files inside templates/:

faculty_form.html
html
Copy
Edit
{% extends "master.html" %}

{% block title %}Add/Update Faculty{% endblock %}

{% block content %}
    <h2>{% if object %}Update{% else %}Add{% endif %} Faculty</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Save</button>
    </form>
{% endblock %}
faculty_list.html
html
Copy
Edit
{% extends "master.html" %}

{% block title %}Faculty List{% endblock %}

{% block content %}
    <h2>Faculty Members</h2>
    <a href="{% url 'faculty_add' %}">Add New Faculty</a>
    <ul>
    {% for faculty in faculties %}
        <li>
            {{ faculty.name }} | {{ faculty.age }} | {{ faculty.qualification }}
            [<a href="{% url 'faculty_update' faculty.id %}">Edit</a>]
            [<a href="{% url 'faculty_delete' faculty.id %}">Delete</a>]
        </li>
    {% empty %}
        <li>No faculty members found.</li>
    {% endfor %}
    </ul>
{% endblock %}
faculty_confirm_delete.html
html
Copy
Edit
{% extends "master.html" %}

{% block title %}Delete Faculty{% endblock %}

{% block content %}
    <h2>Are you sure you want to delete "{{ object.name }}"?</h2>
    <form method="post">
        {% csrf_token %}
        <button type="submit">Yes, Delete</button>
        <a href="{% url 'faculty_list' %}">Cancel</a>
    </form>
{% endblock %}
4. Add URLs in urls.py
In your app’s urls.py:

python
Copy
Edit
from django.urls import path
from .views import FacultyCreateView, FacultyListView, FacultyUpdateView, FacultyDeleteView

urlpatterns = [
    path('faculty/', FacultyListView.as_view(), name='faculty_list'),
    path('faculty/a



# Create your views here.
