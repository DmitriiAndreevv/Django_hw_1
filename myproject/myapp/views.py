import logging
from django.shortcuts import render

logger = logging.getLogger(__name__)

def index(request):
    '''Главная страница.'''
    return render(request,'myapp/index.html')

def about(request):
    """О нас"""
    return render(request,'myapp/about.html')



