from django.shortcuts import render

# Create your views here.


def event_cards(request):
    return render(request, 'test_event_cards.html', {})


def event_row_verify(request):
    return render(request, 'event_row_verify.html', {})


def event_row_condition(request):
    return render(request, 'event_row_condition.html', {})


def event_row_purchase(request):
    return render(request, 'event_row_purchase.html', {})


def event_row_print(request):
    return render(request, 'event_row_print.html', {})
