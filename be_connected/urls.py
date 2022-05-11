from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userapi/', include('user_app.api.urls')),
    path('categoryapi/', include('category_app.api.urls')),
    path('shop_profileapi/', include('shop_profile_app.api.urls')),
]
