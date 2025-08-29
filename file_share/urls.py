# urls.py
from django.contrib import admin
from django.urls import path, include
from accounts.views import (
    HomeView, RegisterView, LoginView, 
    RegisterPageView, CustomAuthToken, logoutview, UserProfilePageView
)
from files.views import FileViewSet, FilesPageView
from rest_framework import routers
from sharing.views import SharedLinkViewSet, SharingPageView, SharedLinkAccessView


router = routers.DefaultRouter()
router.register(r'files', FileViewSet, basename='files')
router.register(r'sharing', SharedLinkViewSet, basename='sharing')


urlpatterns = [
    
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', CustomAuthToken.as_view(), name='login'),
    path('api/profile/', UserProfilePageView.as_view(), name='user-profile'),
    path('api/', include(router.urls)),
    
    
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login-page'),
    path('register/', RegisterPageView.as_view(), name='register-page'),
    path('profile/', UserProfilePageView.as_view(), name='profile-page'),
    path('files/', FilesPageView.as_view(), name='files-page'),
    path('sharing/', SharingPageView.as_view(), name='sharing-page'),
    path('shared/<uuid:token>/', SharedLinkAccessView.as_view(), name='shared-link-access'),
    path('logout/', logoutview, name='logout'),
    
    
    path('admin/', admin.site.urls),
]