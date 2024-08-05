# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    a_id = models.AutoField(primary_key=True)
    a_email = models.CharField(max_length=30, blank=True, null=True)
    a_password = models.CharField(max_length=30)

    def __str__(self):
        return self.a_email

    class Meta:
        managed = False
        db_table = 'admin'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cart(models.Model):
    cart_id = models.IntegerField(primary_key=True)
    cust_id = models.IntegerField(blank=True, null=True)
    p_id = models.IntegerField(blank=True, null=True)
    cart_quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cart'


class Category(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=30, blank=True, null=True)
    c_subcategory = models.CharField(max_length=30, blank=True, null=True)

    
    def __str__(self):
        return self.c_name
    
    class Meta:
        managed = False
        db_table = 'category'


class Customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=10, blank=True, null=True)
    cust_gender = models.CharField(max_length=20, blank=True, null=True)
    cust_email = models.CharField(max_length=30, blank=True, null=True)
    cust_password = models.CharField(max_length=20, blank=True, null=True)
    cust_mobileno = models.CharField(max_length=10, blank=True, null=True)
    cust_addressline1 = models.CharField(max_length=20, blank=True, null=True)
    cust_addressline2 = models.CharField(max_length=100, blank=True, null=True)
    cust_addressline3 = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.cust_name
    
    class Meta:
        managed = False
        db_table = 'customer'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Feedback(models.Model):
    f_id = models.AutoField(primary_key=True)
    f_details = models.CharField(max_length=100, blank=True, null=True)
    cust = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    p = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    o = models.ForeignKey('OrderMaster', models.DO_NOTHING, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'feedback'


class OrderMaster(models.Model):
    o_id = models.AutoField(primary_key=True)
    o_date = models.DateField(blank=True, null=True)
    cust = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    o_status = models.CharField(max_length=49, blank=True, null=True)
    p = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    o_quantity = models.IntegerField(blank=True, null=True)
    o_price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order-master'


class Payment(models.Model):
    p_id = models.AutoField(primary_key=True)
    cust = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    p_amount = models.IntegerField(blank=True, null=True)
    p_paymentmode = models.CharField(max_length=20, blank=True, null=True)
    w = models.ForeignKey('Wholesaler', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment'


class Product(models.Model):
    p_id = models.AutoField(primary_key=True)
    c = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)
    w = models.ForeignKey('Wholesaler', models.DO_NOTHING, blank=True, null=True)
    p_name = models.CharField(max_length=30, blank=True, null=True)
    p_detail = models.TextField(blank=True, null=True)
    p_price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    p_image = models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):
        return self.p_name
    class Meta:
        managed = False
        db_table = 'product'


class Wholesaler(models.Model):
    w_id = models.AutoField(primary_key=True)
    w_name = models.CharField(max_length=50, blank=True, null=True)
    w_email = models.CharField(max_length=40, blank=True, null=True)
    w_password = models.CharField(max_length=40, blank=True, null=True)
    w_mobile_no = models.IntegerField(blank=True, null=True)
    w_address = models.CharField(max_length=300, blank=True, null=True)
    w_image = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.w_name
    
    class Meta:
        managed = False
        db_table = 'wholesaler'
