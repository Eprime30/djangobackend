from django.shortcuts import render
from rest_framework import generics, status
from django.contrib.auth.mixins import LoginRequiredMixin
# from .models import Event
# from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from .serializers import EventSerializer, CategorySerializer
from rest_framework.response import Response
from .models import Event

# Create your views here.


# class EventCreate(LoginRequiredMixin, generic.CreateView):
class EventCreate(generics.GenericAPIView):
    serializer_class = EventSerializer

    def post(self, request):
        event = request.data
        serializer = self.serializer_class(data=event)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        event_data = serializer.data
        event = Event.objects.get(event_data)

        return Response(event_data, status=status.HTTP_201_CREATED)

    # model = Event
    # template_name = 'events/create_form.html'
    # fields = ('category', 'name', 'details', 'venue', 'time', 'date')
    # context_object_name = 'event'
    # success_message = "%(name)s was created successfully"

    class Category(generics.GenericAPIView):
        serializer_class = CategorySerializer

        def post(self, request):
            serializer = self.serializer_class(data=request.data)

            serializer.is_valid(raise_exception=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
