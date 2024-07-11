from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

#http://127.0.0.1:8000/         ->anasayfa
#http://127.0.0.1:8000/home     ->anasayfa
#http://127.0.0.1:8000/kurslar  ->kurs listesi

urlpatterns = [
    path('',include('pages.urls')),
    path('kurslar/',include('courses.urls')),
    path('account/',include('account.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  
