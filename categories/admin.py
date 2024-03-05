from django.contrib import admin
from .import models



class categoryAdmin(admin.ModelAdmin):
    prepopulated_fields= {'slug' : ('name',)}
    list_display=[
        'name','slug'
    ]
# Register your models here.
admin.site.register(models.Category,categoryAdmin)