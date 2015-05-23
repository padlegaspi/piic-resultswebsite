# -*- Coding: utf -8 -*-
#from django.http import HttpResponse

from TasksManager.models import Project # line 1
from django.shortcuts import render

# View for index page.
def page (request):
     action='Display project with client name = "Me"'
     projects_to_me = Project.objects.filter(client_name="Me", title="Project test")
     return render(request, 'en/public/index.html', locals())

#   new_project = Project(title="Tasks Manager with Django",description="Django project to getting start with Django easily.",client_name="Me") # line 2
#   new_project.save() # line 3
#   return render(request, 'en/public/index.html', {'action':'Save datas of model'})


#  all_projects = Project.objects.all()
#  return render(request, 'en/public/index.html', {'action': "Display all project", 'all_projects': all_projects})

#return HttpResponse ("Hello world!")
#  my_hello = "Hello World!"
#  my_variable = "Hello World !"
#  years_old = 15
#  array_city_capitale = [ "Paris", "London", "Washington" ]
#  return render (request, 'en/public/index.html', { "my_var":my_variable, "years":years_old, "array_city":array_city_capitale, "my_hello":my_hello })
# View for connection page. 
# return render(request, 'en/public/connection.html')

