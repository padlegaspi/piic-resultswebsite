# -*- Coding: utf -8 -*-
#from django.http import HttpResponse
from django.shortcuts import render
# View for connection page.
def page (request):
#return HttpResponse ("Hello world!")
#my_hello = "Hello World!"
# my_variable = "Hello World !"
# years_old = 15
# array_city_capitale = [ "Paris", "London", "Washington" ]
# return render (request, 'en/public/index.html', { "my_var":my_variable, "years":years_old, "array_city":array_city_capitale, "my_hello":my_hello })
# View for connection page. 
 return render(request, 'en/public/connection.html')
