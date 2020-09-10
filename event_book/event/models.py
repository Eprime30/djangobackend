from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from user_acc.models import Account

# Create your models here.


class EventCreate(models.Model):

    def create_event(self, name, details, venue, date, time, category, creator, attendees):
        """
        Create and save a Event with the given email and password.
        """
        if not name:
            raise ValueError(_('The Event name must be set'))
        if not details:
            raise ValueError(_('The Detail of the Event must be set'))
        if not venue:
            raise ValueError(_('The Event venue must be set'))
        if not date:
            raise ValueError(_('The Event Date must be set'))
        if not time:
            raise ValueError(_('The Time for the event must be set'))
        if not creator:
            raise ValueError(_('The creator must be set'))
        if not attendees:
            raise ValueError(_('The attendees must be set'))

        event = self.model(
            name=name,
            details=details,
            venue=venue,
            date=date,
            time=time,
            category=category,
            creator=creator,
            attendees=attendees,
        )

        event.save(using=self._db)
        return event


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=500)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Event(models.Model):
    event_title = models.CharField(max_length=150)

    # details = HTMLField('Details')
    venue = models.CharField(max_length=200)
    date = models.DateField(
        help_text='Please use the following format: <em>YYYY-MM-DD</em>.')
    start_time = models.TimeField(
        help_text='Please use the following format: <em>HH:MM:SS<em>')
    end_time = models.TimeField()
    speaker = models.CharField(max_length=150)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='events')
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    attendees = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='attending', blank=True)
    num_of_attendees = models.PositiveIntegerField(default=0, blank=True)
    booking_status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'event'
        verbose_name_plural = 'events'
        ordering = ['date', 'time']

    def get_absolute_url(self):
        return reverse('events:event-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    def get_number_of_attendees(self):
        return self.attendees.all().count()

    def get_comments_number(self):
        return self.comments.all().count()


class Booking(models.Model):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, null=True, blank=True)
    booked_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name="booked")

    def __str__(self):
        return self.booked_by

# class Comment(models.Model):
#     comment = models.TextField(max_length=500)
#     created_date = models.DateField(auto_now=True)
#     created_time = models.TimeField(auto_now=True)
#     event = models.ForeignKey(
#         Event, on_delete=models.CASCADE, related_name='comments')
#     created_by = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     parent = models.ForeignKey(
#         'self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)

#     class Meta:
#         ordering = ('created_date', 'created_time')

#     def get_absolute_url(self):
#         return reverse('comments:comment-detail', kwargs={'pk': self.pk})

#     def __str__(self):
#         return self.comment

#     def get_comment_creator_photo(self):
#         return self.created_by.profile.photo

#     def get_children(self):
#         return self.children.all()

#     def get_parents(self):
#         return self.parent
