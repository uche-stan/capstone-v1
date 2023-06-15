from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    
    path('users', views.UserView.as_view()),
    path('menu-items', views.MenuView.as_view()),
    path('bookings', views.BookingViewSet.as_view()),
    path('api-token-auth/', obtain_auth_token )
]
