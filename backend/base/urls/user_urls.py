from django.urls import path, include
from base.views import user_views as views


urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', views.registerUser, name='reigster'),
    path('profile/', views.getUserProfile, name='userprofile'),
    path('profile/update', views.updateUserProfile, name='user-profile-update'),
    path('', views.getUsers, name='users'),
]