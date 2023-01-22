from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from testapp.models import Student
from django.urls import reverse_lazy
# Create your views here.
class StudentCreate(CreateView):
    model=Student
    fields=['sname','sid','saddress']


class StudentList(ListView):
    model=Student

class StudentDetail(DetailView):
    model=Student

class StudentUpdate(UpdateView):
    model=Student
    fields=['saddress']

class StudentDelete(DeleteView):
    model=Student
    success_url=reverse_lazy('list')

# Create your views here.
