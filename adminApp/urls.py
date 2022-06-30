
from django.urls import path
from adminApp import views

urlpatterns = [
    path('', views.DashboardView.as_view()),
    path('categories',views.CategoryView.as_view()),
    path('sub-cat',views.SubcategoryView.as_view()),
    path('locations',views.LocationView.as_view()),
    path('getlocation',views.getlocation, name='getlocation'),
    path('add_business',views.BusinessView.as_view()),
    path('delete_category/<str:category_id>',views.DeleteCategoryView.as_view()),
    path('edit_category/<str:category_id>', views.EditCategoryView.as_view()),
    path('delete_subcategory/<str:subcategory_id>',views.DeleteSubCategoryViewV.as_view()),
    path('delete-business/<str:business_id>', views.DeleteBusiness.as_view()),
    path('get-sub-category', views.GetSubcategory.as_view()), # AJAX
    path('get-location',views.GetLocation.as_view()),


]