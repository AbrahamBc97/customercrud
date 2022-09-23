from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
  readonly_fields = ('created',)

# Register your models here.
admin.site.register(Customer, CustomerAdmin)