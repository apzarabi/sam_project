from django.http import HttpResponse
from django.shortcuts import render
from events.models import *

def event_cards(request):
    event = Event.objects.get(id=1)
    cat = Category.objects.all()
    #return HttpResponse('<img class="img-responsive img-rounded" src="/media/pictures/77b6026e-b32f-4ae3-bb41-1719dcfca165.JPG">')
    print("here")
    return render(request, 'test_event_cards.html', {'event': event, 'categories': cat})


def event_edit_page(request):
    event = Event.objects.get(id=1)
    return render(request, 'event_edit/event_edit_page.html', {'event': event})


def event_row_verify(request):
    return render(request, 'event_row_parts/event_row_verify.html', {})


def event_row_condition(request):
    return render(request, 'event_row_parts/event_row_condition.html', {})


def event_row_purchase(request):
    return render(request, 'event_row_parts/event_row_purchase.html', {})


def event_row_print(request):
    return render(request, 'event_row_parts/event_row_print.html', {})
