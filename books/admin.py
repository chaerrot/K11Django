from django.contrib import admin
from books.models import Book, Author, Publisher

# Register your models here.
# 관리자모드(admin 페이지)에 테이블이 보이도록 등록한다.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
