from django.contrib import admin

from .models import Login
from .models import Category
from .models import Product_type
from .models import Type_spec
from .models import Employee_register
from .models import Contractor_register
from .models import Vehicle
from .models import Vehicle_pass
from .models import Order_product
from .models import Feedback


admin.site.register(Login)
admin.site.register(Category)
admin.site.register(Product_type)
admin.site.register(Type_spec)
admin.site.register(Employee_register)
admin.site.register(Contractor_register)
admin.site.register(Vehicle)
admin.site.register(Vehicle_pass)
admin.site.register(Order_product)
admin.site.register(Feedback)

# Register your models here.


