from django.contrib import admin
from app.models import Mychats
# Register your models here.

@admin.register(Mychats)
class MychatAdmin(admin.ModelAdmin):
    list_display = ('id','me','frnd','chats')
