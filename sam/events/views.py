# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse

from django.shortcuts import render, redirect
from events.models import *
from django.contrib.auth.decorators import login_required
from .forms import *

def event_cards(request):
    event = Event.objects.get(id=1)
    categories = Category.objects.all()
    return render(request, 'test_event_cards.html', {'event': event, 'categories': categories})

@login_required
def register_event(request):
    """a = Event()
    a.name = "a"
    a.address = "address"
    a.neighborhood = "neghbor"
    a.description = "dscp"
    a.condition = 1
    a.condition_description = "cnd"
    a.latitude = 23
    a.longitude = 19
    a.phone_number = '121212'
    a.subcategory = Subcategory.objects.get(id=1)
    a.dealer = Dealer.objects.get(id=1)
    a.save()"""
    if request.method == "POST":
        eventform = EventForm(request.POST, request.FILES)
        if eventform.is_valid():
            event = eventform.save(commit=False)
            event.condition = 2
            subcat = request.POST.get('subcategory', None)
            print("this has come from form = {}".format(subcat))
            if subcat is None:
                subcat = Subcategory.objects.get(id=1)
            else:
                subcat = Subcategory.objects.get(id=subcat)
            print("f {} {}".format(subcat, subcat.id))
            event.subcategory = subcat
            user_dealer = User.objects.get(username=request.user.username)
            dealer = user_dealer.userinfo.dealer
            print("this is the dealer = {} {}".format(dealer, dealer.id))
            event.dealer = dealer
            event.save()
            i = 0
            while True:
                priceinput = request.POST.get("ticket-price-{}".format(i), None)
                print(priceinput)
                if priceinput is None:
                    break
                countinput = request.POST.get("ticket-num-{}".format(i), None)
                dateinput = request.POST.get("ticket-date-{}".format(i), None)
                nameinput = request.POST.get("ticket-name-{}".format(i), None)
                t = TicketType()
                t.price = priceinput
                t.datetime = dateinput
                t.total = countinput
                t.available = countinput
                t.name = nameinput
                t.event = event
                print('i was here {}'.format(t))
                t.save()
                i += 1
            i=0
            while True:
                print(request.FILES);
                picinput = request.FILES.get("picture-{}".format(i), None)
                print(str(picinput) + "hooooooooooooo")
                if picinput is None:
                    break
                print("???")
                mypic = EventPicture()
                mypic.picture = picinput
                mypic.event = event
                mypic.save()
                i += 1
                print("injaaast :| ")
        else:
            print('didn"t validate')
            return render(request, 'dealer_profile.html', {'categories': Category.objects.all(),
                                                           'eventform': eventform})
    return redirect(reverse('users:show_profile'))




@login_required
def edit_details(request, **kwargs):
    event_id = int(kwargs.pop('event_id'))
    event = Event.objects.get(id=event_id)
    editeventform = EventForm(instance = Event.objects.get(id=event_id))
    errors = {}
    user = request.user
    if request.method == "POST":
            editeventform = EventForm(request.POST, request.FILES)
            if editeventform.is_valid():
                eventForm = EventForm(request.POST, instance=event)
            if not eventForm.is_valid():
                    errors = errors.copy()
                    errors.update(eventForm.errors)
            if not errors:
                myevent = eventForm.save()
                if not user.is_superuser:
                    myevent.condition = 2
                    myevent.save()
                i = 0
                while True:
                    priceinput = request.POST.get("ticket-price-{}".format(i), None)
                    print(priceinput)
                    if priceinput is None:
                        break
                    countinput = request.POST.get("ticket-num-{}".format(i), None)
                    dateinput = request.POST.get("ticket-date-{}".format(i), None)
                    nameinput = request.POST.get("ticket-name-{}".format(i), None)
                    t = TicketType()
                    t.price = priceinput
                    t.datetime = dateinput
                    t.total = countinput
                    t.available = countinput
                    t.name = nameinput
                    t.event = myevent
                    print('i was here {}'.format(t))
                    t.save()
                    i += 1
                i=0
                while True:
                    print(request.FILES);
                    picinput = request.FILES.get("picture-{}".format(i), None)
                    print(str(picinput) + "hooooooooooooo")
                    if picinput is None:
                        break
                    print("???")
                    mypic = EventPicture()
                    mypic.picture = picinput
                    mypic.event = myevent
                    mypic.save()
                    i += 1
                    print("injaaast :| ")
                return redirect(reverse('users:show_profile'))
            else:  # if errors
                return render(request, 'event_edit/event_edit_details.html', {'signup_customer_errors': errors,
                                                     'editeventform': editeventform,
                })
    return render(request, 'event_edit/event_edit_details.html', {'cateogries':Category.objects.all(), 'editeventform':editeventform, 'event':event})


def event_edit_page(request, **kwargs):
    event_id = int(kwargs.pop('event_id'))
    done = int(kwargs.pop('done'))
    event = Event.objects.get(id=event_id)
    return render(request, 'event_edit/event_edit_page.html', {'done': done, 'event': event})


def event_row_verify(request):
    return render(request, 'event_row_parts/event_row_verify.html', {})


def info_template(request, return_url, message):
    return render(request, 'info_template.html', {'return_url':return_url, 'message':message})


def event_row_condition(request):
    return render(request, 'event_row_parts/event_row_condition.html', {})


def event_row_purchase(request):
    return render(request, 'event_row_parts/event_row_purchase.html', {})


def event_row_print(request):
    return render(request, 'event_row_parts/event_row_print.html', {})


def event_view(request, event_id):
    event_id = int(event_id)
    event = Event.objects.get(id=event_id)
    ticket_types = TicketType.objects.filter(event=event)
    categories = Category.objects.all()
    offered_events = event.subcategory.event_set.exclude(id=event.id)[:4]
    return render(request, 'event_page.html', {'offered_events':offered_events,
                                               'event': event,
                                               'ticket_types': ticket_types, 
                                               'categories':categories, 
                                               'side_bar_offer_topic':"از همین زیردسته"})

def show_subcategory(request, **kwargs):
    category_id = int(kwargs.pop('category_id'))
    subcategory_id = int(kwargs.pop('subcategory_id'))
    categories = Category.objects.all()
    if(subcategory_id == 0):
        subcategories = Subcategory.objects.filter(category_id=category_id)
        events = Event.objects.filter(subcategory__in=subcategories).filter(condition=0)
        category = subcategories[0].category
        if len(events) == 0:
            category = None
        subcategory = None
    else:
        events = Event.objects.filter(subcategory=subcategory_id).filter(condition=0)
        category = Subcategory.objects.get(id=subcategory_id).category
        if len(events) == 0:
            subcategory = None
            category = None
        else:
            subcategory = events[0].subcategory
    return render(request, 'subcategory_result.html', {'events': events, 'categories': categories
                                                       , 'category': category, 'subcategory': subcategory})

def delete(request, **kwargs):
    event_id = int(kwargs.pop('event_id'))
    Event.objects.get(id=event_id).delete()
    message = "رویداد مورد نظر حذف شد."
    return_url = reverse('users:show_profile')
    return render(request, 'info_template.html', {'message': message, 'return_url': return_url})

def remove_category(request):
    category_id = request.POST.get("category_id")
    print(category_id)
    Category.objects.get(id=category_id).delete()
    message = "دسته‌ی مورد نظر حذف شد."
    return_url = reverse('users:show_profile')
    print(return_url)
    return render(request, 'info_template.html', {'message': message, 'return_url': return_url})
   
