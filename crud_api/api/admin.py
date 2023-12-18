from django.contrib import admin
from .models import Record
# Register your models here.
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    fields = ['id','name','roll','city']