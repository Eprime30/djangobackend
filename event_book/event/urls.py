from django.urls import path
from .views import EventCreate

app_name = 'event'
urlpatterns = [
    # path('', views.EventList.as_view(), name='event-list'),
    # path('events/<int:pk>/', views.EventDetail.as_view(), name='event-detail'),
    path('event-create/', EventCreate.as_view(), name='event-create'),
    # path('events/<int:pk>/delete', views.EventDelete.as_view(), name='event-delete'),
    # path('events/<int:pk>/update', views.EventUpdate.as_view(), name='event-update'),
    # path('events/<event_id>/attend/', views.attend_event, name='attend_event'),
    # path('events/<event_id>/not_attend/',
    #      views.not_attend_event, name='not_attend_event'),

]
