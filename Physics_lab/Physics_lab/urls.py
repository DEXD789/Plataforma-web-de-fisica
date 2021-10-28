# DJango
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
# Views
from Physics_lab import views as local_views
from labs import views as labs_views
from posts import views as posts_views
from simulations import views as  simulations_views 
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
