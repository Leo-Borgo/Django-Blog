from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_date', 'published_date']
    list_filter = ['created_date', 'published_date', 'author']
    search_fields = ['title', 'content']
    prepopulated_fields = {'title': ('title',)}
    date_hierarchy = 'created_date'
    ordering = ['-created_date']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created_date', 'approved']
    list_filter = ['approved', 'created_date']
    search_fields = ['name', 'content']
    actions = ['approve_comments']
    
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
    approve_comments.short_description = "Aprobar comentarios seleccionados"