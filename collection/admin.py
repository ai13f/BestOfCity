from django.contrib import admin

# Register your models here.
from collection.models import Profile, Restaurant


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Profile, ProfileAdmin)


class RestaurantAdmin(admin.ModelAdmin):
    model = Restaurant
    list_display = ('name', 'description',)
admin.site.register(Restaurant, RestaurantAdmin)
