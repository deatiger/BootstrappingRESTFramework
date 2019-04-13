from django.urls import path, include
from cms import views
from rest_framework import routers
from .views import BookViewSet

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'books', BookViewSet)

app_name = 'cms'

urlpatterns = [
    # Book
    path('', views.book_index, name='book_list'),   # List page
    path('add/', views.book_edit, name='book_add'),  # Register page
    path('mod/<int:book_id>/', views.book_edit, name='book_mod'),  # Modify page
    path('del/<int:book_id>/', views.book_del, name='book_del'),   # Delete page
    path('login/', views.Login.as_view(), name='login'),  # Login page
    path('logout/', views.Logout.as_view(), name='logout'),  # Logout page
]