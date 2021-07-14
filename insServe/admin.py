from django.contrib import admin
from .models import userData,content,comment,collection,like

admin.site.register(userData)
admin.site.register(content)
admin.site.register(comment)
admin.site.register(collection)
admin.site.register(like)