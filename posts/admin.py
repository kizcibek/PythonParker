from django.contrib import admin

# Register your models here.
 #здесь регистрируются модели для их отображения в админ-проекте
from posts.models import Post, Comment


admin.site.register(Post)
admin.site.register(Comment)