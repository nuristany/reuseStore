from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from shop.validators import validate_file_size



class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=20)
    messaging_app_username = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Profile for {self.user.username} {self.user.last_name} {self.user.contact_number}"
    
    def first_name(self):
        return self.user.first_name
    
    def last_name(self):
        return self.user.last_name
    def last_name(self):
        return self.user.last_name
    
    class Meta:
        ordering = ['user__first_name', 'user__last_name']

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Item(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    contact_number = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['title']
        
    def __str__(self):
        return f"{self.title}"

class ItemImage(models.Model):
    item = models.ForeignKey(Item, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shop/images', validators=[validate_file_size])

    def __str__(self):
        return f"Image for {self.item.title} {self.image}"
