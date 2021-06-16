from django.contrib import admin

from book.models import BookModel, CommentModel


@admin.register(BookModel)
class ProductAdminModel(admin.ModelAdmin):
    list_display = ['title', 'is_booked']
    search_fields = ['title']
    readonly_fields = ['is_booked']


@admin.register(CommentModel)
class ProductAdminModel(admin.ModelAdmin):
    list_display = ['text']
    readonly_fields = ['user']
