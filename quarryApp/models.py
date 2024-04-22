from django.db import models

class Login(models.Model):
    log_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.TextField()
    role = models.CharField(max_length=20)
    status = models.IntegerField()
    class Meta:
        db_table = 'tb_Login'


class Category(models.Model):
    ct_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=80)
    class Meta:
        db_table = 'tb_Category'

class Product_type(models.Model):
    tp_id = models.AutoField(primary_key=True)
    ct = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_type = models.CharField(max_length=80)
    stock = models.IntegerField()
    image = models.CharField(max_length=50)
    class Meta:
        db_table = 'tb_Product_type'

class Type_spec(models.Model):
    ts_id = models.AutoField(primary_key=True)
    tp = models.ForeignKey(Product_type,on_delete=models.CASCADE)
    size = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    class Meta:
        db_table = 'tb_Type_spec'

class Employee_register(models.Model):
    emp_id = models.AutoField(primary_key=True)
    log = models.ForeignKey(Login,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    image = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    designation = models.CharField(max_length=50,blank=True,null=True)
    contact_no = models.BigIntegerField()
    email = models.CharField(max_length=50)    
    class Meta:
        db_table = 'tb_Employee_register'

class Contractor_register(models.Model):
    con_id = models.AutoField(primary_key=True)
    log = models.ForeignKey(Login,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    company = models.CharField(max_length=50)
    owner_name = models.CharField(max_length=30)
    licence = models.CharField(max_length=40)
    company_address = models.CharField(max_length=150)
    contact_no = models.BigIntegerField()
    email =  models.CharField(max_length=50)     
    class Meta:
        db_table = 'tb_Contractor_register'

class Vehicle(models.Model):
    v_id = models.AutoField(primary_key=True)
    log = models.ForeignKey(Login,on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=20)
    contact_no = models.BigIntegerField()
    address = models.CharField(max_length=150)
    vehicle_number = models.CharField(max_length=15)
    permit = models.CharField(max_length=50)
    class Meta:
        db_table = 'tb_Vehicle'

class Vehicle_pass(models.Model):
    ps_id = models.AutoField(primary_key=True)
    log = models.ForeignKey(Login,on_delete=models.CASCADE)
    v_id = models.IntegerField()
    date = models.DateField()
    time = models.CharField(max_length=30)
    destination = models.CharField(max_length=150)
    status = models.IntegerField()
    class Meta:
        db_table = 'tb_Vehicle_pass'

class Order_product(models.Model):
    or_id = models.AutoField(primary_key=True)
    log = models.ForeignKey(Login,on_delete=models.CASCADE)
    tp_id = models.IntegerField()
    date = models.DateField()
    re_date = models.DateField()
    size = models.IntegerField()
    load = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True) 
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    o_type = models.CharField(max_length=20)
    status = models.IntegerField()
    class Meta:
        db_table = 'tb_Order_product'

class Feedback(models.Model):
    fd_id = models.AutoField(primary_key=True)
    log_id = models.IntegerField()
    rec_id = models.IntegerField()
    feedback = models.TextField()
    reply = models.TextField()
    feedback_date = models.DateField()
    class Meta:
        db_table = 'tb_Feedback'

# Create your models here.
