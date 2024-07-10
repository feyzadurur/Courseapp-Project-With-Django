from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index),
    path('index',views.index),
    path('contact',views.contact),
    path('about',views.about),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
