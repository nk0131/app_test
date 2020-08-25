from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

class Homeview(TemplateView):
    template_name = 'index.html'

def index(request):
    return render(request, 'test.html')


def test(request):
    return HttpResponse('templates.user.index.html')

