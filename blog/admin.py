from django.contrib import admin
from .models import Article,Category,Archives,Tag
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','created_time','last_modified_time')
    search_fields = ['title']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','created_time','last_modified_time')
    search_fields = ['name']

class ArchivesAdmin(admin.ModelAdmin):
    list_display = ('name','created_time','last_modified_time')
    search_fields = ['name']

class TagAdmin(admin.ModelAdmin):
    list_display = ('name','created_time','last_modified_time')
    search_fields = ['name']

admin.site.register(Article,ArticleAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Archives,ArchivesAdmin)
admin.site.register(Tag,TagAdmin)