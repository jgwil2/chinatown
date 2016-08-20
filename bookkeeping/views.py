from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hell world, welcome to chinatown app')

def book(request, book_id):
    return HttpResponse('You\'re looking at book %s' % book_id)

def expense(request, expense_id):
    return HttpResponse('You\'re looking at expense %s' % expense_id)
