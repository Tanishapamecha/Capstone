from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .models import *
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django import forms

# Create your views here.

# <----------- Login | admin Only------------>
def admin_login(request):
    return render(request,'admin/login/login.html')

def loginsave(request):
    if request.method == 'POST': 
        ademail=request.POST.get('email')
        adpass=request.POST.get('password')
        admin1=Admin.objects.filter(a_email=ademail,a_password=adpass)
        if admin1:
            request.session['a_email']=ademail
            messages.success(request,"you are successfully login")
            return redirect('/home_page/')
        else:
            messages.error(request,"You have Invalid Email or Password")
            return redirect('/admin_login/')
    else:
        return render(request,'admin/login/login.html')

def admin_logout(request):
        logout(request)
        print("not login")
        messages.error(request,"You have successfully logout")
        return redirect('/admin_login/')


# <----------- Master | admin Only------------>
def master_index(request):
    session_data=request.session.get('a_email')
    if session_data:
            print("welcome",session_data)
    else:
                print("not login")
                return redirect('/admin_login/')
    return render(request,'admin/master_index.html')

def home_page(request):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        return render(request,'admin/home_page.html')


# <----------- Category | admin Only------------>


def category_list(request):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        cat=Category.objects.all()
        return render(request,'admin/category/category_list.html',{'cat':cat})

#<------category add function------------------>
def category_add(request):
    session_data=request.session.get('a_email')
    if session_data:
            print("welcome",session_data)
    else:
            print("not login")
            return redirect('/admin_login/')
    return render(request,'admin/category/category_add.html')


def cat_adding(request):
        cat_name=request.POST.get('category_name')
        scat_name=request.POST.get('subcategory_name')

        save_DATA=Category(c_name=cat_name,
                         c_subcategory=scat_name,)
        save_DATA.save()
        return redirect('category_list')

def cat_deleting(request ,id):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        delid=Category.objects.get(c_id=id)
        delid.delete()
        return redirect('category_list')

def cat_updatepage(request, id):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        edit_page=Category.objects.get(c_id=id)
        return render(request,'admin/category/category_edit.html',{'edit':edit_page})


def cat_updating(request,id):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
        cat_name=request.POST.get('category_name')
        scat_name=request.POST.get('subcategory_name')

        save_DATA=Category(c_id=id,
                            c_name=cat_name,
                            c_subcategory=scat_name)
                                
        save_DATA.save()
        return redirect('category_list')

# <----------- Customer | admin Only------------>
def customer_list(request):
    session_data=request.session.get('a_email')
    if session_data:
            print("welcome",session_data)
    else:
            print("not login")
            return redirect('/admin_login/')
    cust=Customer.objects.all()
    return render(request,'admin/customer/customer_list.html',{'cust':cust})


def customer_add(request):
    session_data=request.session.get('a_email')
    if session_data:
            print("welcome",session_data)
    else:
            print("not login")
            return redirect('/admin_login/')
    return render(request,'admin/customer/customer_add.html')


# def adding(request):
#       name=request.POST.get('name')
#       email=request.POST.get('email')
#       Gender=request.POST.get('Gender')
#       pswd=request.POST.get('pswd')
#       mobileno=request.POST.get('mobileno')
#       addressline1=request.POST.get('addressline1')
#       addressline2=request.POST.get('addressline2')
#       addressline3=request.POST.get('addressline3')

#       save_DATA=Customer(cust_name=name,
#                          cust_email=email,
#                          cust_gender=Gender,
#                          cust_password=pswd,
#                          cust_mobileno=mobileno,
#                          cust_addressline1=addressline1,
#                          cust_addressline2=addressline2,
#                          cust_addressline3=addressline3)
#       save_DATA.save()
#       return redirect('customer_list')

def adding(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    Gender = request.POST.get('Gender')
    pswd = request.POST.get('pswd')
    mobileno = request.POST.get('mobileno')
    addressline1 = request.POST.get('addressline1')
    addressline2 = request.POST.get('addressline2')
    addressline3 = request.POST.get('addressline3')

    # Check for None values
    if None not in [name, email, Gender, pswd, mobileno, addressline1, addressline2, addressline3]:
        # Save data if all fields are not None
        save_DATA = Customer(cust_name=name,
                             cust_email=email,
                             cust_gender=Gender,
                             cust_password=pswd,
                             cust_mobileno=mobileno,
                             cust_addressline1=addressline1,
                             cust_addressline2=addressline2,
                             cust_addressline3=addressline3)
        save_DATA.save()
        return redirect('customer_list')
    else:
        # Handle case where some fields are None
        return HttpResponse("Some form fields are empty.")

def deleting(request ,id):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        delid=Customer.objects.get(cust_id=id)
        delid.delete()
        return redirect('customer_list')



def updatepage(request, id):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        edit_page=Customer.objects.get(cust_id=id)
        return render(request,'admin/customer/customer_edit.html',{'edit':edit_page})



def updating(request,id):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
        name=request.POST.get('name')
        email=request.POST.get('email')
        Gender=request.POST.get('Gender')
        pswd=request.POST.get('pswd')
        mobileno=request.POST.get('mobileno')
        addressline1=request.POST.get('addressline1')
        addressline2=request.POST.get('addressline2')
        addressline3=request.POST.get('addressline3')

        save_DATA=Customer(cust_id=id,
                                cust_name=name,
                                cust_email=email,
                                cust_gender=Gender,
                                cust_password=pswd,
                                cust_mobileno=mobileno,
                                cust_addressline1=addressline1,
                                cust_addressline2=addressline2,
                                cust_addressline3=addressline3)
        save_DATA.save()        
        return redirect('customer_list')







# <----------- Feedback | admin Only------------>
def feedback_list(request):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        feed=Feedback.objects.all()
        return render(request,'admin/feedback/feedback_list.html',{'feed':feed})

def feed_deleting(request ,id):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        delid=Feedback.objects.get(f_id=id)
        delid.delete()
        return redirect('feedback_list')


# <----------- Wholesaler | admin Only------------>
def wholesaler_list(request):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        whole=Wholesaler.objects.all()
        return render(request,'admin/wholesaler/wholesaler_list.html',{'whole':whole})

def wholesaler_add(request):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        
        
        return render(request,'admin/wholesaler/wholesaler_add.html')
        
def whole_adding(request):
    session_data = request.session.get('a_email')
    if session_data:
        print("Welcome", session_data)
    else:
        print("Not logged in")
        return redirect('/admin_login/')
    
    name = request.POST.get('name')
    email = request.POST.get('email')
    pswd = request.POST.get('password')
    mobile = request.POST.get('mobile') 
    address = request.POST.get('address')

    # Check if 'image' key exists in request.FILES
    if 'image' in request.FILES:
        image1 = request.FILES['image']
        fss = FileSystemStorage()
        file = fss.save(image1.name, image1)
        file_url = fss.url(file)
    else:
        # Redirect back to the form page with an error message
        return redirect('/wholesaler_list/')
        

    save_DATA = Wholesaler(w_name=name,
                            w_email=email,
                            w_password=pswd,
                            w_mobile_no=mobile,
                            w_address=address,
                            w_image=file_url)
    save_DATA.save()
    return redirect('/wholesaler_list/')


def whole_updatepage(request, id):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        whole=Wholesaler.objects.get(w_id=id)
        return render(request,'admin/wholesaler/wholesaler_edit.html',{'whole':whole})
        
def whole_updating(request, id):
        session_data = request.session.get('a_email')
        if session_data:
                print("Welcome", session_data)
        else:
                print("Not logged in")
                return redirect('/admin_login/')
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        pswd = request.POST.get('password')
        mobile = request.POST.get('mobile') 
        address = request.POST.get('address')

        if 'image' in request.FILES:
                image1 = request.FILES['image']
                fss = FileSystemStorage()
                file = fss.save(image1.name, image1)
                file_url = fss.url(file)
        else:
                return redirect('/wholesaler_list/')
        

        save_DATA = Wholesaler(w_id=id,w_name=name,
                                w_email=email,
                                w_password=pswd,
                                w_mobile_no=mobile,
                                w_address=address,
                                w_image=file_url)
        save_DATA.save()
        return redirect('/wholesaler_list/')

def whole_deleting(request, id):
    session_data = request.session.get('a_email')
    if session_data:
        print("Welcome", session_data)
    else:
        print("Not logged in")
        return redirect('/admin_login/')
    
    try:
        del_id = Wholesaler.objects.get(w_id=id)
        del_id.delete()
        return redirect('wholesaler_list')
    except:
        messages.error(request,"Cannot delete wholesaler because it is referenced by other records.")
        return redirect('/wholesaler_list/')
        





# <----------- Product | admin Only------------>
def product_list(request):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        pro=Product.objects.all()
        return render(request,'admin/product/product_list.html',{'pro':pro})


def product_add(request):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        cat=Category.objects.all()
        whole=Wholesaler.objects.all()

        return render(request,'admin/product/product_add.html',{'cat':cat,'whole':whole})

def pro_adding(request):
        name=request.POST.get('name')

        cat2=request.POST.get('category')
        c_name=Category.objects.get(c_id=cat2)

        whole=request.POST.get('wholesaler')
        w_name=Wholesaler.objects.get(w_id=whole)
        
        # detail=request.POST.get('detail')
        detail = request.POST.get('detail')

        price=request.POST.get('price')


        if 'image' in request.FILES:
            image1 = request.FILES['image']
            fss = FileSystemStorage()
            file = fss.save(image1.name, image1)
            file_url = fss.url(file)
        else:
            return HttpResponse("No image file uploaded.")


        save_DATA=Product(c=c_name,
                                w=w_name,
                                p_name=name,
                                p_detail=detail,
                                p_price=price,
                                p_image=file_url,)
        save_DATA.save()
        return redirect('product_list')

def pro_deleting(request ,id):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        delid=Product.objects.get(p_id=id)
        delid.delete()
        return redirect('product_list')


def pro_updatepage(request, id):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        edit_page=Product.objects.get(p_id=id)
        cat=Category.objects.all()
        whole=Wholesaler.objects.all()
        return render(request,'admin/product/product_edit.html',{'edit':edit_page,'cat':cat,'whole':whole})



def pro_updating(request,id):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
        

        name=request.POST.get('name')
        # detail=request.POST.get('details')
        detail = request.POST.get('details')

        price=request.POST.get('price')

        cat2=request.POST.get('category')
        cat11=Category.objects.get(c_id=cat2)

        whole=request.POST.get('wholesaler')
        w_name=Wholesaler.objects.get(w_id=whole)
        
        detail=request.POST.get('details')
        price=request.POST.get('price')

        if 'image' in request.FILES:
            image1 = request.FILES['image']
            fss = FileSystemStorage()
            file = fss.save(image1.name, image1)
            file_url = fss.url(file)
        else:
            return HttpResponse("No image file uploaded.")

        save_DATA=Product(p_id=id,
                                p_name=name,
                                c=cat11,
                                w=w_name,
                                p_detail=detail,
                                p_price=price,
                                p_image=file_url)
        save_DATA.save()        
        return redirect('product_list')



# <----------- Order master | admin Only------------>
def ordermaster_list(request):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        order=OrderMaster.objects.all()
        return render(request,'admin/ordermaster/ordermaster_list.html',{'order':order})


def ordermaster_add(request):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        cust=Customer.objects.all()
        prio=Product.objects.all()

        return render(request,'admin/ordermaster/ordermaster_add.html',{'cust':cust,'prio':prio})


def order_adding(request):
        Date=request.POST.get('Date')

        cat2=request.POST.get('customer')
        c_name=Customer.objects.get(cust_id=cat2)
        p2=request.POST.get('product')
        product=Product.objects.get(p_id=p2)
        Status=request.POST.get('Status')
        Quantity=request.POST.get('Quantity')
        price=request.POST.get('Price')
        save_DATA=OrderMaster(o_date=Date,
                              cust=c_name,
                              p=product,
                                o_status=Status,
                                o_quantity=Quantity,
                                o_price=price)    
        save_DATA.save()
        return redirect('ordermaster_list')

def order_deleting(request ,id):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        delid=OrderMaster.objects.get(o_id=id)
        delid.delete()
        return redirect('ordermaster_list')

def order_updatepage(request, id):
        session_data=request.session.get('a_email')      
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        edit_page=OrderMaster.objects.get(o_id=id)
        return render(request,'admin/ordermaster/ordermaster_edit.html',{'edit':edit_page})



def order_updating(request,id):
        
        Date=request.POST.get('Date')
        Status=request.POST.get('Status')
        Quantity=request.POST.get('Quantity')
        price=request.POST.get('price')
        save_DATA=OrderMaster(o_date=Date,
                                o_status=Status,
                                o_quantity=Quantity,
                                o_price=price)               
        save_DATA.save()
        return redirect('ordermaster_list')






class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['cart_id', 'cust_id', 'p_id', 'cart_quantity']

def cart_add(request):
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cart_list')
    else:
        form = CartForm()
    return render(request, 'admin/cart/cart_add.html', {'form': form})

def cart_edit(request, cart_id):
    cart = Cart.objects.get(cart_id=cart_id)
    if request.method == 'POST':
        form = CartForm(request.POST, instance=cart)
        if form.is_valid():
            form.save()
            return redirect('cart_list')
    else:
        form = CartForm(instance=cart)
    return render(request, 'admin/cart/cart_edit.html', {'form': form})

def cart_list(request):
    carts = Cart.objects.all()
    return render(request, 'admin/cart/cart_list.html', {'carts': carts})