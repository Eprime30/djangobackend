from django.urls import path
from .views import RegisterView, LoginAPIView
from rest_framework_simplejwt.views import TokenRefreshView
from event import views

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('events/new/', views.EventCreate.as_view(), name='event-create'),

]
