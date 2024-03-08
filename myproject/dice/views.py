from django.http import HttpResponse
from  random import choice,randint
import logging

logger = logging.getLogger(__name__)

# Create your views here.

def coin(request):
    side = choice (['орёл', 'решка'])
    logger.debug(side)
    return HttpResponse(side)

def dice(request):
    count=randint(1, 6)
    logger.debug(count)
    return HttpResponse(count)

def hundred(request):
    number = randint(1, 100)
    logger.debug(number)
    return HttpResponse(number)


