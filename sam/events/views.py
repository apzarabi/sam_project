from django.shortcuts import render

# Create your views here.


def event_small_card(request):
    return render(request, 'event_small_card.html', {})


def event_row_verify(request):
    return render(request, 'event_row_verify.html', {})