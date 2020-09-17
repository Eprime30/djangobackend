# # Register your models here.
# from django.contrib import admin


# from event.models import Booking, Event

from .models import (
    Event,
    Booking,

)
from django.contrib import admin

admin.site.site_header = 'Event Booking Admin'
admin.site.site_title = 'The Admin Dashboard'
admin.site.index_title = 'Welcome to this Portal'

# class BookAdmin(admin.ModelAdmin):
#     list_display = ('event', 'time', 'user')
#     search_fields = ('event', 'user')

#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()


# class EventAdmin(admin.ModelAdmin):
#     list_display = ('topic', 'time', 'venue',
#                     'room_capacity', 'speaker', 'tagline')
#     search_fields = ('topic', 'speaker', 'tagline')

#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()


# admin.site.register(Booking, BookAdmin)
# admin.site.register(Event, EventAdmin)


admin.site.register(Event)
admin.site.register(Booking)
