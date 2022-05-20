from django.urls import path

from shop_profile_app.api import views


urlpatterns = [
    path('shop_profile/', views.Shop_profileView.as_view(), name='profile'),
    path('shop_profile_edit/<pk>/',views.shop_profile_edit.as_view(),name='profile_edit'),
    # path('logout/',views.logout_view, name='logout'),
    
]