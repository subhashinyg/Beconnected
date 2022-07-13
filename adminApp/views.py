from urllib import response
from django.contrib import messages
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from requests import Response, delete, get
from stripe import Order
from category_app.models import *
from .forms import locationviewform
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
class DashboardView(View):
    def get(self,request):
        return render(request, 'dashboard.html')

class CategoryView(View):
    def get(self, request):
        try:
            template = 'category.html'
            cat = Category.objects.all().order_by('pk')
            menu = 'category'
            return render(request, template, context={
                'category': cat,
                'menu': menu,
            })
        except Exception as e:
            messages.add_message(request, messages.WARNING, 'Something went wrong. Error: '+str(e))
            return HttpResponseRedirect(redirect_to='dashboard')

    def post(self, request):
        try:
            category = request.POST['category']
            cat_name = Category.objects.create(category_name=category)
            cat_name.save()
            message = 'Category added successfully!'
            messages.add_message(request, messages.SUCCESS, message)
        except Exception as e:
            messages.add_message(request, messages.WARNING, 'Failed to save Category. Error: '+str(e))
        finally:
            return HttpResponseRedirect(redirect_to='categories')

class EditCategoryView(View):
    def get(self, request, category_id):
        try:
            edit_category = Category.objects.get(pk=category_id)
            template = 'category.html'
            heading = 'Edit Category'
            edit_category.save()
            return render(request, template, context={
                'heading': heading,
                'edit_category': edit_category,
                'category_id': category_id
            })
            
        except Exception as e:
            return HttpResponse(str(e))

class DeleteCategoryView(View):
    def get(self, request, category_id):
        try:
            delete_category = Category.objects.filter(pk=category_id).delete()
            if (delete_category):
                messages.add_message(request, messages.SUCCESS, 'Category deleted successfully!')
            else:
                messages.add_message(request, messages.WARNING, 'There is no such category exists to delete')
            return HttpResponseRedirect(redirect_to='/categories')
        except Exception as e:
            return HttpResponse(str(e))

class SubcategoryView(View):
    
    def get(self, request):
        try:
            template = 'sub_category.html'
            cat = Category.objects.all().order_by('pk')
            sub_cat = SubCategory.objects.all().order_by('pk')
            menu = 'sub_category'
            return render(request, template, context={
                'sub_category': sub_cat,
                'cat':cat,
                'menu': menu,
            })
        except Exception as e:
            messages.add_message(request, messages.WARNING, 'Something went wrong. Error: '+str(e))
            return HttpResponseRedirect(redirect_to='dashboard')

    
    def post(self, request):
        try:
            category = request.POST['categories_id']
            print(category,'////////catgory//////')
            sub_category = request.POST['subcategory']
            print(sub_category,'//////////////')
            obj=SubCategory.objects.create(categories_id=category,subcategory_name=sub_category)           
            obj.save()         
            message = 'Sub Category added successfully!'
            messages.add_message(request, messages.SUCCESS, message)
        except Exception as e:
            messages.add_message(request, messages.WARNING, 'Failed to save SubCategory. Error: '+str(e))
        finally:
            return HttpResponseRedirect(redirect_to='/sub-cat')

class DeleteSubCategoryViewV(View):
    def get(self, request, subcategory_id):
        try:
            delete_subcategory = SubCategory.objects.filter(pk=subcategory_id).delete()
            if(delete_subcategory):
                messages.add_message(request, messages.SUCCESS, 'Sub Category deleted successfully!')
            else:
                messages.add_message(request, messages.WARNING, 'There is no such category exists to delete')
            return HttpResponseRedirect(redirect_to='/sub-cat')
        except Exception as e:
            return HttpResponse(str(e))


def getlocation(request):
    qs = list(Locations.objects.values())
    return JsonResponse({'data':qs})

class LocationView(View):
    def get(self,request):       
        template = 'locations.html'
        location = Locations.objects.all().distinct('location_name')      
        category = Category.objects.all().order_by('pk') 
         
        return render(request, template, context={
            'location':location,
            'category': category,
            
        })
    

    
    def post(self, request):
        try:
            category = request.POST['categories_id']
            sub_cat = request.POST['sub_categories_id']
            location = request.POST['location']
            print(category, sub_cat, location)
            obj=Locations
            try:
                subobj= SubCategory.objects.get(id=sub_cat)
                catobj= Category.objects.get(id=category)
            except:
                return HttpResponse({"error":"category_id or subcategory_id not available"})
            #Locations.objects.create(category=category, subcategories=sub_cat, location_name=location)
            obj(subcategories=subobj,category=catobj,location_name=location).save()
            # print(obj)
            # obj.save()
            
            # lc(subcategories=sub_cat,category=category,location_name=location)
            # lc.save()

            message = 'Locations added sucessfully'
            print(message,"/////////////////////////////////")
            messages.add_message(request, messages.SUCCESS, message)
        except Exception as e:
            messages.add_message(request, messages.WARNING, 'Failed to save Location. Error: '+str(e))
        finally:
            return HttpResponseRedirect(redirect_to='locations')


class BusinessView(View):
    def get(self,request):       
        template = 'business_add.html'
        category = Category.objects.all()
        subcategory =SubCategory.objects.all()
        business = BusinessServices.objects.all() 
        location= Locations.objects.all()       
        return render(request, template, context={
            'business': business,
            'category':category,
            'subcategory':subcategory,
            'location':location
        })
    def post(self, request):
        print('hellooooooooo')
        try:
            category = request.POST['categories_id']
            print(category,'category')
            sub_cat = request.POST['sub_categories_id']
            print(sub_cat,'sub_cat')
            location = request.POST['location']
            print(sub_cat,'location')
            business_name = request.POST['business_name']
            print(business_name,'business_name')
            description = request. POST['description']
            print(description,'description')
            address = request.POST['address']
            print(address,'address')
            phone = request.POST['phone']  
            print(phone,'phone') 
            landline_no =request.POST['landline_no']
            print(landline_no,'landline_no')
            website = request.POST['website']
            print(website,'website')
            instagram = request.POST['instagram']
            print(instagram,'instagram')
            twitter = request.POST['twitter']
            print(twitter,'twitter')
            facebook = request.POST['facebook']
            print(facebook,'facebook')
            linkedin = request.POST['linkedin']
            print(linkedin,'linkedin')
            image = request.POST['image']
            googlemap=request.POST['googlemap']
            print(category, sub_cat, location)
            obj = BusinessServices.objects.create(category_id=category, subcategory_id=sub_cat, location_id=location,name=business_name,description=description,
            address=address,phone_no=phone,landline_no=landline_no,website=website,instagram=instagram,twitter=twitter,facebook=facebook,linkedin=linkedin,image=image,googlemap=googlemap)
            obj.save()
            message = 'Business added sucessfully'
            messages.add_message(request, messages.SUCCESS, message)
        except Exception as e:
            messages.add_message(request, messages.WARNING, 'Failed to save BusinessServices. Error: '+str(e))
        finally:
            return HttpResponseRedirect(redirect_to='add_business')

class DeleteBusiness(View):
    def get(self, request, business_id):
        try:
            delete_business = BusinessServices.objects.filter(pk=business_id).delete()
            if(delete_business):
                messages.add_message(request, messages.SUCCESS, 'Sub Category deleted successfully!')
            else:
                messages.add_message(request, messages.WARNING, 'There is no such category exists to delete')
            return HttpResponseRedirect(redirect_to='/add_business')
        except Exception as e:
            return HttpResponse(str(e))

#ajax request for get category
class GetSubcategory(View):
    def post(self, request):
        category_id =request.POST.get('categoryId')
        
        sub_categories = SubCategory.objects.filter(categories=category_id)
        
        return render(request, 'subcategory_dropdownlist.html', {'sub_categories': sub_categories})
        # return JsonResponse(list(cities.values('id', 'name')), safe=False)


#ajax request for get location
class GetLocation(View):
    def post(self, request):
        category_id =request.POST.get('categoryId')
        subcategory_id= request.POST.get('subcategoryId')
        location = Locations.objects.filter(category=category_id,subcategories=subcategory_id)
        
        return render(request, 'location_dropdown.html', {'location': location})
        # return JsonResponse(list(cities.values('id', 'name')), safe=False)