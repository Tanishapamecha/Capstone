from django.urls import path
from Bizease_app import views
from Bizease import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [

# <------------------admin Only------------------>



# <----------- Login | admin Only------------>
    path('admin_login/',views.admin_login,name="admin_login"),
    path('loginsave/',views.loginsave,name="loginsave"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),


    #  path('admin_login/',views.admin_login,name="admin_login"),
    path('master_index/',views.master_index,name="master_index"),
    path('home_page/',views.home_page,name="home_page"),


# <----------- Category data | admin Only------------>

    path('category_list/',views.category_list,name="category_list"),
    path('category_add/',views.category_add,name="category_add"),
    path('cat_adding/',views.cat_adding,name="cat_adding"),
    path('cat_deleting/<int:id>/',views.cat_deleting,name="cat_deleting"),
    path('cat_updatepage/<int:id>/',views.cat_updatepage,name="cat_updatepage"),
    path('cat_updating/<int:id>/',views.cat_updating,name="cat_updating"),




   
# <----------- Customer data | admin Only------------>
    path('customer_list/',views.customer_list,name="customer_list"),
    path('customer_add/',views.customer_add,name="customer_add"),
    path('adding/',views.adding,name="adding"),
    path('deleting/<int:id>/',views.deleting,name="deleting"),
    path('updatepage/<int:id>/',views.updatepage,name="updatepage"),
    path('updating/<int:id>/',views.updating,name="updating"),




# <----------- Wholesaler data | admin Only------------>

    path('wholesaler_list/',views.wholesaler_list,name="wholesaler_list"),
    path('wholesaler_add/',views.wholesaler_add,name="wholesaler_add"),
    path('whole_adding/',views.whole_adding,name="whole_adding"),
    path('whole_deleting/<int:id>/',views.whole_deleting,name="whole_deleting"),
    path('whole_updatepage/<int:id>/',views.whole_updatepage,name="whole_updatepage"),
    path('whole_updating/<int:id>/',views.whole_updating,name="whole_updating"),



# <----------- Feedback data | admin Only------------>
    path('feedback_list/',views.feedback_list,name="feedback_list"),
    path('feed_deleting/<int:id>/',views.feed_deleting,name="feed_deleting"),
    # path('feed_updatepage/<int:id>/',views.feed_updatepage,name="feed_updatepage"),
    # path('feed_updating/<int:id>/',views.feed_updating,name="feed_updating"),




# <----------- ordermaster data | admin Only------------>
    path('ordermaster_list/',views.ordermaster_list,name="ordermaster_list"),
    path('ordermaster_add/',views.ordermaster_add,name="ordermaster_add"),
    path('order_adding/',views.order_adding,name="order_adding"),
    path('order_deleting/<int:id>/',views.order_deleting,name="order_deleting"),
    path('order_updatepage/<int:id>/',views.order_updatepage,name="order_updatepage"),
    path(' /<int:id>/',views.order_updating,name="order_updating"),







# <----------- Product data | admin Only------------>
    path('product_list/',views.product_list,name="product_list"),
    path('product_add/',views.product_add,name="product_add"),
    path('pro_adding/',views.pro_adding,name="pro_adding"),
    path('pro_deleting/<int:id>/',views.pro_deleting,name="pro_deleting"),
    path('pro_updatepage/<int:id>/',views.pro_updatepage,name="pro_updatepage"),
    path('pro_updating/<int:id>/',views.pro_updating,name="pro_updating"),



# <----------- CART data | admin Only------------>

    path('admin/cart/add/', views.cart_add, name='cart_add'),
    path('admin/cart/<int:cart_id>/edit/', views.cart_edit, name='cart_edit'),
    path('admin/cart/', views.cart_list, name='cart_list'),








]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

