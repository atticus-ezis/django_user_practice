from django.urls import path, include
from django.contrib.auth import views
from .views import profile, signup, profile_redirect

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', signup, name='signup'),
    path('profile-redirect/', profile_redirect, name='profile-redirect'),
    path('<str:username>/', profile, name='profile'),
    
    path('<str:username>/notes/', include('notes.urls')),
]
