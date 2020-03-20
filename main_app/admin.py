from django.contrib import admin

# Register your models here.

from django.contrib import admin
# import your models here
from .models import Dog, Walks

# Register your models here
admin.site.register(Dog)
admin.site.register(Walks)
