from django.contrib import admin
from django.urls import path
from calculator.views import recipe_view, main_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page),
    path('<recipe_name>/', recipe_view),
]
