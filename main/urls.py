 


from django.contrib import admin
from django.urls import path
from django.conf import settings  # Important import
from django.conf.urls.static import static # Important import
from . import views 

urlpatterns = [
    # This makes home.html the first page you see
    path('', views.home_view, name='home'),
    
    # This keeps your universal converter working in the background
    path('convert/', views.universal_converter, name='convert_action'),
    
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Add this at the very end, outside the urlpatterns list
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)