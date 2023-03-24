from django.contrib import admin

from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
 
    # add the fields of the model here
    list_display = ("title","completed")

admin.site.register(Task, TaskAdmin)