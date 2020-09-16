from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from user_acc.models import Account
import datetime
from django.utils import timezone

# Create your models here.


class Event(models.Model):
    topic = models.CharField(max_length=200)
    time_choice = (
        ('Morning', 'Morning'),
        ('Midmorning', 'Midmorning'),
        ('Afternoon', 'Afternoon'),
    )
    time = models.CharField(max_length=30, blank=False, choices=time_choice)
    venue = models.CharField(max_length=100)
    room_capacity = models.PositiveIntegerField()
    speaker = models.CharField(max_length=50)
    tagline = models.CharField(max_length=100)

    def __str__(self):
        return self.topic


# Create your models here.


# class Event(models.Model):
#     title = models.CharField(max_length=100)
#     location = models.CharField(max_length=100)
#     morning = 'Morning'
#     midmorning = 'Midmorning'
#     afternoon = 'Afternoon'
#     EVENT_TIME_CHOICES = [
#         (morning, 'Morning'),
#         (midmorning, 'Midmorning'),
#         (afternoon, 'Afternoon'),
#     ]
#     event_time = models.CharField(max_length=15, choices=EVENT_TIME_CHOICES)
#     speaker = models.CharField(max_length=100)
#     topic = models.CharField(max_length=300)
#     roomcapacity = models.CharField(max_length=50)
#     description = models.TextField()
#     image = models.ImageField(upload_to='uploads/')

#     def __str__(self):
#         return self.title

# class Event(models.Model):

#     topic = models.CharField(max_length=150)
#     # times = (
#     #     ('Morning', 'Morning'),
#     #     ('Midmorning', 'Midmorning'),
#     #     ('Afternoon', 'Afternoon'),
#     # )
#     venue = models.CharField(max_length=200, default="home")

#     # time = models.CharField(verbose_name='time', max_length=50,
#     #                         choices=times, default='')

#     date = models.DateField(
#         help_text='Please use the following format: <em>YYYY-MM-DD</em>.')
#     speaker = models.CharField(max_length=150)
#     room_capacity = models.IntegerField()
#     seat_number = models.IntegerField(default=0)

#     class Meta:
#         verbose_name = 'event'
#         verbose_name_plural = 'events'
#         ordering = ['date']

#     # def get_absolute_url(self):
#     #     return reverse('events:event-detail', kwargs={'pk': self.pk})
#     def get_total_capacity(self):
#         total = room_capacity
#         # for b in self.event:
#         #     total += b.capacity
#         return total

#     def get_total_attend(self):
#         total_attend = 0
#         for b in self.event:
#             total_attend += len(b.users_attendance)
#         return total_attend

#     def get_attendance(self):
#         total_attend = self.get_total_attend()
#         total = self.get_total_capacity()

#     def __str__(self):
#         return self.topic

#     def get_number_of_attendees(self):
#         return self.attendees.all().count()

    # def get_comments_number(self):
    #     return self.comments.all().count()


# @property
# def bookings_total(self):
#     return self.bookings_set.filter(bookingstatus='y').count()

# @property
# def bookings_left(self):
#     return self.bookings_total - self.seats


class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    times = (
        ('Morning', 'Morning'),
        ('Midmorning', 'Midmorning'),
        ('Afternoon', 'Afternoon'),
    )

    time = models.CharField(verbose_name='time', max_length=50,
                            choices=times, default='')

    def __str__(self):
        return str(self.user) + " For " + str(self.event)

    # class Meta:
    #     verbose_name = 'Attendee for event'
    #     verbose_name_plural = 'Attendees for events'
    #     ordering = ['time']
    #     unique_together = ('event', 'user')

    # def add_user_to_list_of_attendees(self, user):
    #     registration = Booking.objects.create(
    #         user=user, event=self, time_registered=timezone.now())
    #     registration.add()

    # def remove_user_from_list_of_attendees(self, user):
    #     registration = Booking.objects.get(user=user, event=self)
    #     registration.delete()

    # def save(self, *args, **kwargs):
    #     if self.id is None and self.time_registered is None:
    #         self.time_registered = datetime.datetime.now()
    #     super(Booking, self).save(*args, **kwargs)
