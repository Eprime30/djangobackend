from rest_framework import serializers
from event.models import Event, Booking


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        # fields = ['topic', 'venue', 'date', 'speaker', 'room_capacity']
        exclude = []


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        exclude = []

    def validate_event(self, value):
        if value:
            # event = Event.objects.get(pk=value)
            if value.room_capacity <= Booking.objects.count():
                raise serializers.ValidationError(
                    {"Fully Booked": "All seated have been allocated"})
        return value
