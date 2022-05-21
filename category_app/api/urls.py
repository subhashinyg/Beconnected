from django.urls import path

from category_app.api import views


urlpatterns = [
    path('categories/', views.CategoryView.as_view(), name='category'),
    path('categories/<int:pk>/',views.Categoryupdate.as_view(),name='categoryedit'),
    path('sub_categories/',views.SubCategoryView.as_view(),name='subcategory'),
    path('locations/',views.LocationView.as_view(),name='location'),
    path('getSubcategory/<pk>/',views.Subcategory, name='get_subcategory'),
    path('business-services', views.BusinessServicesView.as_view()),
    #path('shop_description', views.ShopDescriptionView.as_view(), name='shop_description')
    #path('logout/',views.logout_view, name='logout'),
    

]