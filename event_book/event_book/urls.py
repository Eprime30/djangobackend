"""event_book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from event_book.view import dashboard  # , login_page, logut_page
from . import settings

# schema_view = get_schema_view(
#     openapi.Info(
#         title="EVENT BOOKING API",
#         default_version='v1',
#         description="Test description",
#         terms_of_service="https://www.ourapp.com/policies/terms/",
#         contact=openapi.Contact(email="contact@events.local"),
#         license=openapi.License(name="Test License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_acc.urls')),
    path('event/', include('event.urls')),
    path('dash/', dashboard, name='dashboard'),
    # path('login/', login_page, name='login'),
    # path('logout/', logut_page, name='logout'),
    # path('', schema_view.with_ui('swagger',
    #                              cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc',
    #                                    cache_timeout=0), name='schema-redoc')
]
