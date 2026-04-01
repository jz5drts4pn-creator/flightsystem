from django.contrib import admin
from django.urls import path
from accounts.views import home  # 👈 import your real view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # 👈 homepage now uses accounts view
]