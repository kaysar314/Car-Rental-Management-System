from django.contrib import admin
from .models import Car, Offer, Deal, Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('car', 'daily_rental', 'fetch_date', 'return_date')

@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ('offer', 'tenant', 'fetch_date', 'return_date', )

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    # verbose_name_plural = 'owners'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

