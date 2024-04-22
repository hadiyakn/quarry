from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.hashers import make_password
from .models import *
from django.contrib import messages
from django.db import connection
from django.contrib.auth import logout
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse

cursor = connection.cursor()

def home(request):
    if 'user' in request.session:
        user = request.session['user']
        data = Login.objects.get(username=user)
        if data.role == 'admin':
            return render(request,'master/home.html')
        elif data.role == 'contractor':
            return redirect('/contractor_home')
        elif data.role == 'employee':
            return render(request, 'employee/home.html')
        else:
            return redirect('/home')
    else:
        return render(request,'home.html')
    
def index(request):
    if 'user' in request.session:
        user = request.session['user']
        data = Login.objects.get(username=user)
        if data.role == 'admin':
            return render(request,'master/index.html')
        elif data.role == 'contractor':
            return redirect('/contractor_home')
        elif data.role == 'employee':
            return render(request, 'employee/index.html')
        else:
            return redirect('/home')
    else:
        return render(request,'home.html')

def login(request):
    if request.method == 'POST':
        use = request.POST['use']
        pas = request.POST['pas']
        try:
            data = Login.objects.get(username=use,password= pas)
            if data.status == 1:
                request.session['user'] = use
                request.session['log_id'] = data.log_id
                return redirect('/home')
            else:
                messages.success(request, 'Admin Approval required...')
                return redirect(login)
        except Exception:
            messages.success(request, 'Invalid Username Or Password...')
            return redirect(login)
    else:
        return render(request,'login.html')
    
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


#-----------------Master-------------------
def category(request):
    if 'user' in request.session:
        if request.method == 'POST':
            cat = request.POST['n1']
            Category.objects.create(category=cat)
            messages.success(request,'Category added successfully.....')
            return redirect('/category')
        else:
            d = Category.objects.all()
            return render(request,'master/product_category.html',{'data':d})
    else:
        return redirect('/home')
    
def up_category(request,ct_id):
    if 'user' in request.session:
        data=Category.objects.filter(ct_id=ct_id)
        return render(request,'master/up_category.html',{'data':data})
    else:
        return redirect('/home')
    
def update_category(request):
    if 'user' in request.session:
        if request.method == 'POST':
            id = request.POST['n1']
            cat = request.POST['n2']
            Category.objects.filter(ct_id=id).update(category=cat)
            messages.success(request, 'Updated successfully.....')
            return redirect('/category')
        else: 
            return redirect('/category')
    else:
        return redirect('/home')
    
def del_category(request,ct_id):
    if 'user' in request.session:
        data  = Category.objects.get(ct_id=ct_id)
        data.delete()
        messages.success(request, 'Category deleted successfully.....')
        return redirect ('/category')
    else:
        return redirect('/home')

def product_type(request):
    if 'user' in request.session:
        if request.method == 'POST':
            ct_id = request.POST['n1']
            p_type =  request.POST['n2']
            n4 = request.FILES['n4']

            obj = FileSystemStorage()
            fl = obj.save(n4.name,n4)
            img = obj.url(fl)

            Product_type.objects.create(ct_id=ct_id,product_type=p_type,stock=0,image=img)
            messages.success(request,'Product type added successfully.....')
            return redirect('/product_type')
        else:
            d = Category.objects.all()
            d2 = Product_type.objects.all().select_related('ct')
            return render(request,'master/product_type.html',{'data':d,'data2':d2})
    else:
        return redirect('/home')
    
def up_type(request,tp_id):
    if 'user' in request.session:
        data = Product_type.objects.filter(tp_id=tp_id).select_related('ct')
        data2 = Category.objects.all()
        return render(request,'master/up_type.html',{'data':data,'data2':data2})
    else:
        return redirect('/home')
    
def update_type(request):
    if 'user' in request.session:
        if request.method == 'POST':
            ct_id = request.POST['n1']
            p_type =  request.POST['n2']
            tp_id = request.POST['tp_id']
            if len(request.FILES) == 0:

                Product_type.objects.filter(tp_id=tp_id).update(ct_id=ct_id,product_type=p_type)
                messages.success(request,'Updated successfully.....')
                return redirect('/product_type')
            else:
                n4 = request.FILES['n4']
                obj = FileSystemStorage()
                fl = obj.save(n4.name,n4)
                img = obj.url(fl)

                Product_type.objects.filter(tp_id=tp_id).update(ct_id=ct_id,product_type=p_type,image=img)
                messages.success(request,'Updated successfully.....')
                return redirect('/product_type')
        else:
            return redirect('/product_type')
    else:
        return redirect('/home')
    
def del_type(request,tp_id):
    if 'user' in request.session:
        data  = Product_type.objects.get(tp_id=tp_id)
        data.delete()
        messages.success(request, 'Deleted successfully.....')
        return redirect ('/product_type')
    else:
        return redirect('/home')

def type_spec(request):
    if 'user' in request.session:
        if request.method == 'POST':
            tp_id = request.POST['n1']
            siz =  request.POST['n2']
            pri = request.POST['n3']

            Type_spec.objects.create(tp_id=tp_id,size=siz,price=pri)
            messages.success(request,'Added successfully.....')
            return redirect('/type_spec')
        else:
            d = Product_type.objects.all()
            d2 = Type_spec.objects.all().select_related('tp')
            return render(request,'master/product_price.html',{'data':d,'data2':d2})
    else:
        return redirect('/home')
    
def up_spec(request,ts_id):
    if 'user' in request.session:
        data = Type_spec.objects.filter(ts_id=ts_id).select_related('tp')
        data2 = Product_type.objects.all()
        return render(request,'master/update_price.html',{'data':data,'data2':data2})
    else:
        return redirect('/home')
    
def update_spec(request):
    if 'user' in request.session:
        if request.method == 'POST':
            ts_id = request.POST['n1']
            tp_id = request.POST['n2']
            siz = request.POST['n3']
            pri = request.POST['n4']

            Type_spec.objects.filter(ts_id=ts_id).update(tp_id=tp_id,size=siz,price=pri)
            messages.success(request, 'Updated successfully.....')
            return redirect('/type_spec')
        else:
            return redirect('/type_spec')
    else:
        return redirect('/home')
    
def del_spec(request,ts_id):
    if 'user' in request.session:
        data  = Type_spec.objects.get(ts_id=ts_id)
        data.delete()
        messages.success(request, 'Deleted successfully.....')
        return redirect ('/type_spec')
    else:
        return redirect('/home')
    
def emp_register(request):
    if 'user' in request.session:
        if request.method == 'POST':
            nam = request.POST['n1']
            n2 = request.FILES['n2']

            obj = FileSystemStorage()
            fl = obj.save(n2.name,n2)
            img = obj.url(fl)

            add = request.POST['n3']
            con = request.POST['n4']
            ema = request.POST['n5']
            use = request.POST['n6']
            desi = request.POST['n9']
            
            pas =  request.POST['n7']

            Login.objects.create(username=use,password=pas,role='employee',status=1)
            d = Login.objects.get(username=use)

            Employee_register.objects.create(name=nam,image=img,address=add,contact_no=con,designation=desi,email=ema,log_id=d.log_id)
            messages.success(request, 'Registered successfully.....')
            return redirect('/emp_register')
        else:
            data = Employee_register.objects.all()
            return render(request,'master/emp_register.html',{'data':data})
    else:
        return redirect('/home')
    
def del_emp(request,log_id):
    if 'user' in request.session:
        data  = Login.objects.get(log_id=log_id)
        data.delete()
        messages.success(request, 'Employee deleted successfully.....')
        return redirect ('/emp_register')
    else:
        return redirect('/home')
    
def view_contractor(request):
    if 'user' in request.session:
        data  = Contractor_register.objects.all().select_related('log')
        return render (request,'master/view_contractor.html',{'data':data})
    else:
        return redirect('/home')
    
def approve_contractor(request,log_id):
    if 'user' in request.session:
        Login.objects.filter(log_id=log_id).update(status=1)
        return redirect('/view_contractor')
    else:
        return redirect('/home')
    
def del_contractor(request,log_id):
    if 'user' in request.session:
        data  = Login.objects.get(log_id=log_id)
        data.delete()
        messages.success(request, 'Deleted successfully.....')
        return redirect ('/view_contractor')
    else:
        return redirect('/home')

def order_view(request):
    if 'log_id' in request.session:
        cursor.execute("select c.name,c.company,tp.product_type,o.date,o.re_date,o.size,o.price,o.load,o.amount,o.status,o.or_id from tb_product_type as tp inner join tb_order_product as o on o.tp_id=tp.tp_id inner join tb_contractor_register as c on c.log_id=o.log_id where o.o_type='order'")
        data = cursor.fetchall()
        return render(request,'master/order_view.html',{'data':data})
    else:
        return redirect('/home')

def buy_view(request):
    if 'log_id' in request.session:
        cursor.execute("select c.name,c.company,tp.product_type,o.date,o.re_date,o.size,o.price,o.load,o.amount,o.status from tb_product_type as tp inner join tb_order_product as o on o.tp_id=tp.tp_id inner join tb_contractor_register as c on c.log_id=o.log_id where o.o_type='buy'")
        data = cursor.fetchall()
        return render(request,'master/buy_view.html',{'data':data})
    else:
        return redirect('/home')

def pass_view(request):
    if 'log_id' in request.session:
        cursor.execute("select  v.owner_name,v.vehicle_number,v.permit,p.date,p.time,p.destination,p.status,p.ps_id from tb_vehicle as v inner join tb_vehicle_pass as p on v.v_id=p.v_id")
        data = cursor.fetchall()
        return render(request,'master/pass_view.html',{'data':data})
    else:
        return redirect('/home')

def reply(request):
    if 'log_id' in request.session:
        if request.method == 'POST':
            fd_id = request.POST['fd_id']
            rep = request.POST['rep']
            Feedback.objects.filter(fd_id=fd_id).update(reply=rep)
            messages.success(request, 'Replied successfully.....')
            return redirect('/reply')
        else:
            cursor.execute("select c.name,f.* from tb_contractor_register as c inner join tb_feedback as f on c.log_id=f.log_id")
            data = cursor.fetchall()
            return render(request,'master/view_feedback.html',{'data':data})
    else:
        return redirect('/home')

def ad_profile(request):
    if 'log_id' in request.session:
        log_id = request.session['log_id']
        if request.method == 'POST':
            logid = request.POST['n1']
            opas = request.POST['n2']
            npas = request.POST['n3']
            try:
                data = Login.objects.get(log_id=logid)
                if data.password == opas:
                    Login.objects.filter(log_id=logid).update(password=npas)
                    messages.success(request, 'Your Password has been Reset successfully.....')
                    return redirect('/ad_profile')
                else:
                    messages.success(request, 'Enter valid current password....!')
                    return redirect('/ad_profile')
            except Exception:
                messages.success(request, 'Invalid User.....')
                return redirect('/ad_profile')
        else:
            data = Login.objects.filter(log_id=log_id)
            return render(request,'master/profile.html',{'data':data})
    else:
        return redirect('/login')



    

#------------------Employee-------------------

def add_stock(request):
    if 'user' in request.session:
        data = Product_type.objects.all().select_related('ct')
        return render(request,'employee/add_stock.html',{'data':data})
    else:
        return redirect('/home')

def up_stock(request,tp_id):
    if 'user' in request.session:
        data=Product_type.objects.filter(tp_id=tp_id)
        return render(request,'employee/update_stock.html',{'data':data})
    else:
        return redirect('/home')
    
def update_stock(request):
    if 'user' in request.session:
        if request.method == 'POST':
            tp_id = request.POST['tp_id']
            sto = request.POST['sto']
            Product_type.objects.filter(tp_id=tp_id).update(stock=sto)
            messages.success(request, 'Stock Updated successfully.....')
            return redirect('/add_stock')
        else: 
            return redirect('/add_stock')
    else:
        return redirect('/home')

def order_details(request):
    if 'log_id' in request.session:
        cursor.execute("select c.name,c.company,tp.product_type,o.date,o.re_date,o.size,o.price,o.load,o.amount,o.status,o.or_id from tb_product_type as tp inner join tb_order_product as o on o.tp_id=tp.tp_id inner join tb_contractor_register as c on c.log_id=o.log_id where o.o_type='order'")
        data = cursor.fetchall()
        return render(request,'employee/order_details.html',{'data':data})
    else:
        return redirect('/home')
    
def buy_details(request):
    if 'log_id' in request.session:
        cursor.execute("select c.name,c.company,tp.product_type,o.date,o.re_date,o.size,o.price,o.load,o.amount,o.status,o.or_id from tb_product_type as tp inner join tb_order_product as o on o.tp_id=tp.tp_id inner join tb_contractor_register as c on c.log_id=o.log_id where o.o_type='buy'")
        data = cursor.fetchall()
        return render(request,'employee/buy_details.html',{'data':data})
    else:
        return redirect('/home')

def deliver(request,or_id):
    if 'user' in request.session:
        Order_product.objects.filter(or_id=or_id).update(status=1)
        messages.success(request, 'Updated successfully.....')
        return redirect('/home')
    else:
        return redirect('/home')
    
def view_pass_request(request):
    if 'log_id' in request.session:
        log_id = request.session['log_id']
        cursor.execute("select  v.owner_name,v.vehicle_number,v.permit,p.date,p.time,p.destination,p.status,p.ps_id from tb_vehicle as v inner join tb_vehicle_pass as p on v.v_id=p.v_id")
        data = cursor.fetchall()
        return render(request,'employee/pass_request.html',{'data':data})
    else:
        return redirect('/home')  
    

def approve_pass(request,ps_id):
    if 'user' in request.session:
        Vehicle_pass.objects.filter(ps_id=ps_id).update(status=1)
        return redirect('/view_pass_request')
    else:
        return redirect('/home')
    
def reject_pass(request,ps_id):
    if 'user' in request.session:
        Vehicle_pass.objects.filter(ps_id=ps_id).update(status=2)
        return redirect('/view_pass_request')
    return redirect('/home')

def emp_profile(request):
    if 'log_id' in request.session:
        log_id = request.session['log_id']
        if request.method == 'POST':
            logid = request.POST['logid']
            nam = request.POST['n1']
            add = request.POST['n3']
            cno = request.POST['n4']
            ema = request.POST['n5']

            if len(request.FILES) == 0:
                Employee_register.objects.filter(log_id=logid).update(name=nam,address=add,contact_no=cno,email=ema)
                messages.success(request, 'Updated successfully.....')
                return redirect('/emp_profile')
            else:
                n2 = request.FILES['n2']
                obj = FileSystemStorage()
                fl = obj.save(n2.name,n2)
                img = obj.url(fl)

                Employee_register.objects.filter(log_id=logid).update(name=nam,address=add,contact_no=cno,email=ema,image=img)
                messages.success(request, 'Updated successfully.....')
                return redirect('/emp_profile')
        else:
            data = Employee_register.objects.filter(log_id=log_id)
            return render(request,'employee/profile.html',{'data':data})
    else:
        return redirect('/home')

def reset_emp(request):
    if 'log_id' in request.session:
        log_id = request.session['log_id']
        if request.method == 'POST':
            logid = request.POST['logid']
            opas = request.POST['opas']
            npas = request.POST['npas']
            try:
                data = Login.objects.get(log_id=logid)
                if data.password == opas:
                    Login.objects.filter(log_id=logid).update(password=npas)
                    messages.success(request, 'Your Password has been Reset successfully.....')
                    return redirect('/emp_profile')
                else:
                    messages.success(request, 'Enter valid current password....!')
                    return redirect('/reset_emp')
            except Exception:
                messages.success(request, 'Invalid User.....')
                return redirect('/reset_emp')
        else:
            data = Login.objects.filter(log_id=log_id)
            return render(request,'employee/reset_emp.html',{'data':data})
    else:
        return redirect('/home')  


#--------------contractor-----------

def contractor_reg(request):
    if request.method == 'POST':
        nam = request.POST['n1']
        cnam = request.POST['n2']
        onam = request.POST['n3']

        n4 = request.FILES['n4']

        obj = FileSystemStorage()
        fl = obj.save(n4.name,n4)
        lic = obj.url(fl)

        cadd = request.POST['n5']
        con = request.POST['n6']
        ema = request.POST['n7']
        use = request.POST['n8']
        
        pas =  request.POST['n9']

        Login.objects.create(username=use,password=pas,role='contractor',status=0)
        d = Login.objects.get(username=use)

        Contractor_register.objects.create(name=nam,company=cnam,owner_name=onam,licence=lic,company_address=cadd,contact_no=con,email=ema,log_id=d.log_id)
        messages.success(request, 'Registered successfully.....')
        return redirect('/contractor_reg')
    else:
        return render(request,'contractor_reg.html')
    
def contractor_home(request):
    if 'user' in request.session:
        data = Product_type.objects.all().select_related('ct')
        return render(request,'contractor/home.html',{'data':data})
    else:
        return redirect('/home')

def add_vehicle(request):
    if 'log_id' in request.session:
        log_id = request.session['log_id']
        if request.method == 'POST':
            onam = request.POST['n1']
            con = request.POST['n2']
            add = request.POST['n3'] 
            vno = request.POST['n4']
            per = request.POST['n5']
            Vehicle.objects.create(owner_name=onam,contact_no=con,address=add,vehicle_number=vno,permit=per,log_id=log_id)
            messages.success(request, 'Added successfully.....')
            return redirect('/add_vehicle')
        else:
            data = Vehicle.objects.filter(log_id=log_id)
            return render(request,'contractor/vehicle_details.html',{'data':data})
    else:
        return redirect('/home')

def up_vehicle(request,v_id):
    if 'user' in request.session:
        data=Vehicle.objects.filter(v_id=v_id)
        return render(request,'contractor/update_vehicle.html',{'data':data})
    else:
        return redirect('/home')

def update_vehicle(request):
    if 'log_id' in request.session:
        if request.method == 'POST':
            v_id = request.POST['v_id']
            onam = request.POST['n1']
            con = request.POST['n2']
            add = request.POST['n3'] 
            vno = request.POST['n4']
            per = request.POST['n5']
            Vehicle.objects.filter(v_id=v_id).update(owner_name=onam,contact_no=con,address=add,vehicle_number=vno,permit=per)
            messages.success(request, 'Updated successfully.....')
            return redirect('/add_vehicle')
        else:
           return redirect('/add_vehicle')
    else:
        return redirect('/home')


def del_vehicle(request,v_id):
    if 'user' in request.session:
        data  = Vehicle.objects.get(v_id=v_id)
        data.delete()
        messages.success(request, 'Deleted successfully.....')
        return redirect ('/add_vehicle')
    else:
        return redirect('/home')

def pass_request(request):
    if 'log_id' in request.session:
        log_id = request.session['log_id']
        if request.method == 'POST':
            v_id = request.POST['v_id']
            dt = request.POST['n1']
            n2 = request.POST['n2'] 
            n3 = request.POST['n3']

            tim = n2+' - '+n3
            des = request.POST['n4']

            Vehicle_pass.objects.create(log_id=log_id,v_id=v_id,date=dt,time=tim,destination=des,status=0)
            messages.success(request, 'Applied successfully.....')
            return redirect('/pass_request')
        else:
            data = Vehicle.objects.filter(log_id=log_id)
            return render(request,'contractor/pass_request.html',{'data':data})
    else:
        return redirect('/home')

def view_pass(request):
    if 'log_id' in request.session:
        log_id = request.session['log_id']
        cursor.execute("select  v.owner_name,v.vehicle_number,v.permit,p.date,p.time,p.destination,p.status from tb_vehicle as v inner join tb_vehicle_pass as p on v.v_id=p.v_id where p.log_id="+str(log_id))
        data = cursor.fetchall()
        return render(request,'contractor/view_pass.html',{'data':data})
    else:
        return redirect('/home')  

def order(request,tp_id):
    if 'user' in request.session:
        data  = Product_type.objects.filter(tp_id=tp_id)
        data2  = Type_spec.objects.filter(tp_id=tp_id)
        return render(request,'contractor/order_product.html',{'data':data,'data2':data2})
    else:
        return redirect('/home')

def buy(request,tp_id):
    if 'user' in request.session:
        data  = Product_type.objects.filter(tp_id=tp_id)
        data2  = Type_spec.objects.filter(tp_id=tp_id)
        return render(request,'contractor/buy_product.html',{'data':data,'data2':data2})
    else:
        return redirect('/home')

def order_product(request):
    if 'user' in request.session:
        if request.method == 'POST':
            tp_id = request.POST['tp_id']
            size = request.POST['size']
            data  = Product_type.objects.filter(tp_id=tp_id)
            data2 = Type_spec.objects.filter(tp_id=tp_id,size=size)
            return render(request,'contractor/order_now.html',{'data':data,'data2':data2})
        else:
            return redirect('/home')
    else:
        return redirect('/home')

def order_now(request):
    if 'log_id' in request.session:
        log_id = request.session['log_id']
        if request.method == 'POST':
            tp_id = request.POST['tp_id']
            from datetime import date
            dt = date.today()
            rdt = request.POST['rdt']
            size = request.POST['size']
            load = request.POST['lod']
            pri = request.POST['price']
            amt = request.POST['amnt']
           
            Order_product.objects.create(log_id=log_id,tp_id=tp_id,date=dt,re_date=rdt,size=size,load=load,price=pri,amount=amt,o_type='order',status=0)
            messages.success(request, 'Ordered successfully.....')

            return redirect('/home')
        else:
            return redirect('/home')
    else:
        return redirect('/home')  

def view_order(request):
    if 'log_id' in request.session:
        log_id = request.session['log_id']
        cursor.execute("select c.name,c.company,tp.product_type,o.date,o.re_date,o.size,o.price,o.load,o.amount,o.status from tb_product_type as tp inner join tb_order_product as o on o.tp_id=tp.tp_id inner join tb_contractor_register as c on c.log_id=o.log_id where o.o_type='order' and c.log_id="+str(log_id))
        data = cursor.fetchall()
        return render(request,'contractor/view_order.html',{'data':data})
    else:
        return redirect('/home')

def buy_product(request):
    if 'user' in request.session:
        if request.method == 'POST':
            tp_id = request.POST['tp_id']
            size = request.POST['size']
            data  = Product_type.objects.filter(tp_id=tp_id)
            data2 = Type_spec.objects.filter(tp_id=tp_id,size=size)
            return render(request,'contractor/buy_now.html',{'data':data,'data2':data2})
        else:
            return redirect('/home')
    else:
        return redirect('/home')
    
def buy_now(request):
    if 'log_id' in request.session:
        log_id = request.session['log_id']
        if request.method == 'POST':
            tp_id = request.POST['tp_id']
            from datetime import date
            dt = date.today()
            rdt = request.POST['rdt']
            size = request.POST['size']
            load = request.POST['lod']
            pri = request.POST['price']
            amt = request.POST['amnt']

            s = int(load)*int(size)
            d=Product_type.objects.get(tp_id=tp_id)
            sub = d.stock-s
            
            Product_type.objects.filter(tp_id=tp_id).update(stock=sub)
            Order_product.objects.create(log_id=log_id,tp_id=tp_id,date=dt,re_date=rdt,size=size,load=load,price=pri,amount=amt,o_type='buy',status=0)
            messages.success(request, 'Ordered successfully.....')

            return redirect('/home')
        else:
            return redirect('/home')
    else:
        return redirect('/home')  

def view_buy(request):
    if 'log_id' in request.session:
        log_id = request.session['log_id']
        cursor.execute("select c.name,c.company,tp.product_type,o.date,o.re_date,o.size,o.price,o.load,o.amount,o.status from tb_product_type as tp inner join tb_order_product as o on o.tp_id=tp.tp_id inner join tb_contractor_register as c on c.log_id=o.log_id where o.o_type='buy' and c.log_id="+str(log_id))
        data = cursor.fetchall()
        return render(request,'contractor/view_buy.html',{'data':data})
    else:
        return redirect('/home')


def contractor_profile(request):
    if 'log_id' in request.session:
        log_id = request.session['log_id']
        if request.method == 'POST':
            logid = request.POST['n7']
            nam = request.POST['n1']
            cnam = request.POST['n2']
            onam = request.POST['n3']
            add = request.POST['n4']
            cno = request.POST['n5']
            ema = request.POST['n6']

            Contractor_register.objects.filter(log_id=logid).update(name=nam,company=cnam,owner_name=onam,company_address=add,contact_no=cno,email=ema)
            return redirect('/contractor_profile')
        else:
            data = Contractor_register.objects.filter(log_id=log_id)
            return render(request,'contractor/profile.html',{'data':data})
    else:
        return redirect('/home')

def contractor_feedback(request):
    if 'log_id' in request.session:
        log_id = request.session['log_id']
        if request.method == 'POST':
            data = Login.objects.get(role='admin')
            re_id = data.log_id
            from datetime import date
            dt = date.today()
            feed = request.POST['feed']
            Feedback.objects.create(log_id=log_id,rec_id=re_id,feedback=feed,reply='0',feedback_date=dt)
            messages.success(request, 'Feedback sended successfully.....')
            return redirect('/contractor_feedback')
        else:
            cursor.execute("select c.name,f.* from tb_contractor_register as c inner join tb_feedback as f on c.log_id="+str(log_id))
            data = cursor.fetchall()
            return render(request,'contractor/feedback.html',{'data':data})
    else:
        return redirect('/home')

def reset_con(request):
    if 'log_id' in request.session:
        log_id = request.session['log_id']
        if request.method == 'POST':
            logid = request.POST['logid']
            opas = request.POST['opas']
            npas = request.POST['npas']
            try:
                data = Login.objects.get(log_id=logid)
                if data.password == opas:
                    Login.objects.filter(log_id=logid).update(password=npas)
                    messages.success(request, 'Your Password has been Reset successfully.....')
                    return redirect('/contractor_profile')
                else:
                    messages.success(request, 'Enter valid current password....!')
                    return redirect('/contractor_profile')
            except Exception:
                messages.success(request, 'Invalid User.....')
                return redirect('/contractor_profile')
        else:
            data = Login.objects.filter(log_id=log_id)
            return render(request,'contractor/reset_con.html',{'data':data})
    else:
        return redirect('/home')  




def master_reg(request):
    if request.method == 'POST':
        use = request.POST['use']
        pas =  request.POST['pas']
        Login.objects.create(username=use,password=pas,role='admin',status=1)
        return redirect('/master_reg')
    else:
        return render(request,'master_reg.html')
    
def sign_out(request):
    logout(request)
    request.session.delete()
    return redirect('/home')

# Create your views here.
