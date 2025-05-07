from . import views
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.views.i18n import set_language
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", views.index, name="index"),
    path('ajax/check-user/', views.check_user_exists, name='check_user_exists'),
    path('set-language/', set_language, name='set_language'),
    path('i18n/', include('django.conf.urls.i18n')),  # ✅ Required for /i18n/setlang/
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)