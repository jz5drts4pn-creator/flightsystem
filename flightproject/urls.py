from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # login/logout templates
    path('accounts/', include('accounts.urls')),            # your app routes
    path('', include('accounts.urls')),                     # homepage at root
]