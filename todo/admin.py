from django.contrib import admin

# Register your models here.
from .models import Folder, Task#追加

admin.site.register(Folder)
admin.site.register(Task)#追加
