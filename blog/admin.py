from django.contrib import admin
from blog.models import Article, Comments

# Register your models here.
class ArticleInline(admin.StackedInline):
	model = Comments
	extra = 2

class ArticleAdmin(admin.ModelAdmin):
	inlines = [ArticleInline]


admin.site.register(Article, ArticleAdmin)
