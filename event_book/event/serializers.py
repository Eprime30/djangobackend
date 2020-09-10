from rest_framework import serializers
from event.models import Event, Category
# from .models import Comment


# class CommentSerializer(serializers.HyperlinkedModelSerializer):
#     event = serializers.HyperlinkedRelatedField(
#         read_only=True, view_name='event-detail')
#     created_by = serializers.HyperlinkedRelatedField(
#         read_only=True, view_name='comment-detail')

#     class Meta:
#         model = Comment
#         fields = ('id', 'url', 'comment', 'created_date',
#                   'created_time', 'event', 'created_by')

# class EventSerializer(serializers.HyperlinkedModelSerializer):
class EventSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.name')
    creator = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='event-detail')
    attendees = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='event-detail')
    # comments = CommentSerializer(read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'event_title', 'venue', 'date',
                  'start_time', 'end_time', 'speaker', 'category', 'creator', 'attendees', 'booking_status']

    def create(self):
        return Event.objects.create_event


# class CategorySerializer(serializers.HyperlinkedModelSerializer):
class CategorySerializer(serializers.ModelSerializer):
    events = EventSerializer(read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'description')
