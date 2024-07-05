from django.contrib import admin
from django.urls import path,include

#http://127.0.0.1:8000/         ->anasayfa
#http://127.0.0.1:8000/home     ->anasayfa
#http://127.0.0.1:8000/kurslar  ->kurs listesi

urlpatterns = [
    path('',include('pages.urls')),
    path('kurslar/',include('courses.urls')),
    path('admin/', admin.site.urls),
]
