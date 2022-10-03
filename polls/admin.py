from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

from django.contrib.auth.admin import UserAdmin


class platform_Admin(admin.ModelAdmin):
    actions=['add_action_to_this_plat']
    def add_action_to_this_plat(self,request,queryset):
        for j in queryset:
            data.objects.filter(name=j.name).update(color1=j.color1,color2=j.color2,image=j.image,form_id=j.id,domain=j.domain)
        self.message_user(request,'update data successfully')
    # Other stuff here
    def has_delete_permission(self, request, obj=None):
        return False
    def delete_model(self, request, obj):
        pass    



# UserAdmin.list_display = ('username','email', 'is_active', 'is_staff')

class MyUserAdmin(UserAdmin):
     list_display = ('username','email', 'is_active','verify', 'is_staff')

     def verify(self,obj):
        k=Profile.objects.get(user=obj.id)
        return k.Isverified


admin.site.unregister(User)

admin.site.register(User, MyUserAdmin)


# Register your models here.
admin.site.register(Profile)
admin.site.register(Playstore_config_class)
admin.site.register(appstore_config_class)
admin.site.register(config)
admin.site.register(Vcard)
admin.site.register(Custom_button)
admin.site.register(platforms,platform_Admin)
admin.site.register(favorite)
admin.site.register(data)




    
    




#############################################################
admin.site.register(title)
admin.site.register(header)
admin.site.register(html)

admin.site.register(contact_form)
admin.site.register(RSS_Feed)
admin.site.register(Link)
admin.site.register(product)
admin.site.register(IMAGE)
