from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user_app.api import views


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('register/',views.user_registration_view,name='register'),
    #path('logout/',views.logout_view, name='logout'),
    
    

]