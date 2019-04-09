from django.urls import path
from cms import views
from django.urls import include
from rest_framework import routers
from .views import BookViewSet


# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
# router.register('impression', views.ImpressionViewSet)

app_name = 'cms'
urlpatterns = [
    # Book
    path('book/', views.BookList.as_view(), name='book_list'),   # 一覧
    path('book/add/', views.book_edit, name='book_add'),  # 登録
    path('book/mod/<int:book_id>/', views.book_edit, name='book_mod'),  # 修正
    path('book/del/<int:book_id>/', views.book_del, name='book_del'),   # 削除
]