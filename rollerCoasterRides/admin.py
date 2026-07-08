from django.contrib import admin
# from django.contrib import admin
from .models import User, Ride, Booking

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone_number', 'role', 'created_at']
    search_fields = ['username', 'email']
    list_filter = ['role']

@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'capacity', 'price_per_slot', 'status']
    search_fields = ['name']
    list_filter = ['category', 'status']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'ride', 'booking_date', 'time_slot', 'num_tickets', 'total_price', 'status']
    search_fields = ['user__username', 'ride__name']
    list_filter = ['status', 'booking_date']
# from .models import Author,Book
# admin.site.register(Author)
# admin.site.register(Book)