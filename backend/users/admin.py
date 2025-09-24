from django.contrib import admin
from .models import User, Address, Company


admin.site.register(User)
admin.site.register(Address)
admin.site.register(Company)

