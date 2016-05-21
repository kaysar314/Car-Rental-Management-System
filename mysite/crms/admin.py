from django.contrib import admin
from .models import Deal, Profile, Offer
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.

class DealAdmin(admin.ModelAdmin):
    list_display = ('offer', 'tenant', 'pub_date', )

class OfferAdmin(admin.ModelAdmin):
    list_display = ('owner', 'car_name', 'daily_rental', 'time', )

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    # verbose_name_plural = 'owners'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Deal, DealAdmin)
