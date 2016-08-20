from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
class Index(View):
    def get(self, request):
        return HttpResponse('Hell world, welcome to chinatown app')

class Book(View):
    def get(self, request, book_id):
        return HttpResponse('You\'re looking at book %s' % book_id)

class Expense(View):
    def get(self, request, expense_id):
        return HttpResponse('You\'re looking at expense %s' % expense_id)
