from atexit import register
from django.contrib import admin
from .models import Post , Category , Profil,Coment


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profil)
admin.site.register(Coment)