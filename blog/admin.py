from django.contrib import admin
from blog.models import Article,UserInfo
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date')
class AdviceAdmin(admin.ModelAdmin):
    list_display = ('username','advice')
admin.site.register(Article,ArticleAdmin)
admin.site.register(UserInfo,AdviceAdmin)
