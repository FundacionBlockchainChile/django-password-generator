from django.shortcuts import render
import random
# from django.http import HttpResponse


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def contact(request):
  return render(request, 'contact.html')

def email(request):
  return render(request, 'email.html')

def password(request):
  characters = list('abcdefghijklmnopqrstvwxyz')
  generated_password = ''
  length = int(request.GET.get('length'))
  
  if request.GET.get('uppercase'):
    characters.extend('ABCDEFGHIJKLMNOPQRSTVWXYZ')
  if request.GET.get('special'):
    characters.extend('$#_%&/()')
  if request.GET.get('numbers'):
    characters.extend('123456789')
  
  for x in range(length):
    generated_password += random.choice(characters)
  
  return render(request, 'password.html', {'password': generated_password})
