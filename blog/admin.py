from django.contrib import admin


from .models import Post

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ['title']}

admin.site.register(Post, PostAdmin)

