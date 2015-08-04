# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from events.models import *

def event_cards(request):
    event = Event.objects.get(id=1)
    categories = Category.objects.all()
    return render(request, 'test_event_cards.html', {'event': event, 'categories': categories})


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


def event_view(request, event_id):
    event_id = int(event_id)
    event = Event.objects.get(id=event_id)
    categories = Category.objects.all()
    offered_events = event.subcategory.event_set.exclude(id=event.id).filter(pk__in=[0, 1, 2, 3, 4, 5])
    return render(request, 'event_page.html', {'offered_events':offered_events, 'event': event, 'categories':categories, 'side_bar_offer_topic':"از همین زیردسته"})


def show_subcategory(request, **kwargs):
    subcategory_id = int(kwargs.pop('subcategory_id'))
    categories = Category.objects.all()
    events = Event.objects.filter(subcategory=subcategory_id)
    if(len(events) != 0):
        category = Subcategory.objects.get(id=subcategory_id).category.name
        subcategory = Subcategory.objects.get(id=subcategory_id).name
    return render(request, 'subcategory_result.html', {'events': events, 'categories': categories
                                                       , 'category': category, 'subcategory': subcategory})

