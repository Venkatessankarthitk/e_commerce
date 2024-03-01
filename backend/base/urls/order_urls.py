from django.urls import path, include
from base.views import user_views as views


urlpatterns = [
    path('', views.getUsers, name='users'),
]