from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from django.contrib.auth.mixins import LoginRequiredMixin

from .serializers import EventSerializer, BookingSerializer
from rest_framework.response import Response
from .models import Event, Booking
from user_acc.models import Account
from django.http import HttpResponse, Http404

# Create your views here.


class EventCreate(generics.GenericAPIView):

    serializer_class = EventSerializer

    def post(self, request):
        event = request.data
        serializer = self.serializer_class(data=event)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        event_data = serializer.data
        event = Event.objects.get(topic=event_data['topic'])

        return Response(event_data, status=status.HTTP_201_CREATED)


class BookingView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def post(self, request):
        book = request.data
        serializer = self.serializer_class(data=book)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        book_data = serializer.data
        # book = Booking.objects.get(event=book_data['event'])

        return Response(book_data, status=status.HTTP_201_CREATED)


class EventView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class BookedEventsView(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class EventsBookedByUser(APIView):
    def get(self, request, pk, format=None):
        try:
            u = Account.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        qs = u.booking_set.all().values_list("event", flat=True)
        qs = Event.objects.filter(pk__in=qs)
        events = EventSerializer(qs, many=True)
        return Response(events.data)


class EventAttendees(APIView):
    def get(self, request, pk):
        event = Event.objects.get(pk=pk)
        bookingset = Booking.objects.filter(event=event)
        events = BookingSerializer(bookingset, many=True)
        return Response(events.data)
