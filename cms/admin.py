from cms.models import Book
from django.contrib import admin


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'publisher', 'page')  # 一覧に出したい項目
    list_display_links = ('id', 'name',)  # 修正リンクでクリックできる項目


admin.site.register(Book, BookAdmin)

