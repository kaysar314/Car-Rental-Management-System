from django.contrib import admin
from .models import Car, Offer, Deal, Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner')

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'car', 'daily_rental', 'fetch_date', 'return_date')

@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ('id', 'offer', 'get_offer_owner', 'tenant', 'fetch_date', 'return_date', 'is_accept')

    def get_offer_owner(self, obj):
        return obj.offer.car.owner.username
    get_offer_owner.admin_order_field = 'offer'
    get_offer_owner.short_description = 'owner'

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    # verbose_name_plural = 'owners'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )
    list_display = ('id', 'username', 'email', 'is_staff', 'last_login')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

