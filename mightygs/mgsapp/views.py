# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Student
# Create your views here.

def index(request):
	try:
	    student_list = Student.objects.all()
	    context = {'student_list' : student_list}
	except Student.DoesNotExist:
		raise Http404("Student does not exist")
	return render(request, 'mgsapp/index.html', context)
def go(request):
	return render(request, 'mgsapp/go.html')

