from django.urls import path
from django.contrib.auth import views
from .views import profile, signup

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile')
]
