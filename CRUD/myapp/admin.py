from django.contrib import admin

from myapp.models import registermodel, category


# Register your models here.


class showregistermodel(admin.ModelAdmin):
    list_display = ["id", "name", "email", "phone", "password", "address", "user_photo", "gender", "role"]

admin.site.register(registermodel,showregistermodel)

class showcategory(admin.ModelAdmin):
    list_display = ["id", "catname"]
    
admin.site.register(category,showcategory)