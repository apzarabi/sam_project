from django.contrib import admin
from .models import *

admin.site.register((Category, Subcategory, Event, EventPicture, TicketType, Ticket, Order, Comment, Rate))