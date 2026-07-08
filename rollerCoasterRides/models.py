from django.db import models

from django.urls import reverse

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


# ── User Table ─────────────────────────────────────────────────────────────
class User(AbstractUser):
    ROLE_CHOICES = [
        ('visitor', 'Visitor'),
        ('admin',   'Admin'),
    ]
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    role         = models.CharField(max_length=10, choices=ROLE_CHOICES, default='visitor')
    date_of_birth = models.DateField(null=True, blank=True)
    created_at   = models.DateTimeField(auto_now_add=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='rollercoaster_users',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='rollercoaster_users',
        blank=True
    )

    def __str__(self):
        return f"{self.username} ({self.role})"

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])


# ── Ride Table ─────────────────────────────────────────────────────────────
class Ride(models.Model):
    CATEGORY_CHOICES = [
        ('thrill',   'Thrill'),
        ('family',   'Family'),
        ('kids',     'Kids'),
        ('water',    'Water'),
    ]
    STATUS_CHOICES = [
        ('available',    'Available'),
        ('maintenance',  'Under Maintenance'),
        ('closed',       'Closed'),
    ]
    name           = models.CharField(max_length=100)
    category       = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description    = models.TextField()
    capacity       = models.PositiveIntegerField(help_text="Max riders per session")
    duration_mins  = models.PositiveIntegerField(help_text="Duration in minutes")
    min_height_cm  = models.PositiveIntegerField(null=True, blank=True, help_text="Minimum height in cm")
    price_per_slot = models.DecimalField(max_digits=8, decimal_places=2)
    status         = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    image          = models.ImageField(upload_to='rides/', null=True, blank=True)
    created_at     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.category})"

    def get_absolute_url(self):
        return reverse('ride-detail', args=[str(self.id)])

    def is_available(self):
        return self.status == 'available'


# ── Booking Table ──────────────────────────────────────────────────────────
class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending',    'Pending'),
        ('confirmed',  'Confirmed'),
        ('cancelled',  'Cancelled'),
        ('completed',  'Completed'),
    ]
    user           = models.ForeignKey(User,    on_delete=models.CASCADE, related_name='bookings')
    ride           = models.ForeignKey(Ride,    on_delete=models.CASCADE, related_name='bookings')
    booking_date   = models.DateField()
    time_slot      = models.TimeField(help_text="Preferred time slot")
    num_tickets    = models.PositiveIntegerField(default=1)
    total_price    = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    status         = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    booked_at      = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-booked_at']
        # prevent double booking same slot by same user
        unique_together = ('user', 'ride', 'booking_date', 'time_slot')

    def save(self, *args, **kwargs):
        # Auto-calculate total price before saving
        self.total_price = self.ride.price_per_slot * self.num_tickets
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} → {self.ride.name} on {self.booking_date}"

    def get_absolute_url(self):
        return reverse('booking-detail', args=[str(self.id)])

# class Author(models.Model):
#     name = models.CharField(max_length = 100)
#     birthdate = models.DateField(null = True,blank = True)

#     def _str_(self):
#         return self.name
    
# class Book(models.Model):
#         title = models.CharField(max_length=200)
#         author = models.ForeignKey(Author,on_delete= models.CASCADE)
#         summary = models.TextField()
#         isbn = models.CharField(max_length=13,unique=True)
#         published_date = models.DateField(auto_now_add=True)
#         price = models.DecimalField(max_digits=6,decimal_places=2)
#         def _str_(self):
#               return self.title
        
#         def get_absolute_url(self):
#             return reverse('book-detail',args = [str(self.id)])    
        

