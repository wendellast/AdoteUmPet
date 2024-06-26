from allauth.socialaccount.providers.google.urls import (
    urlpatterns as google_urlpatterns,
)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

social_urlpatterns = [
    path("", include(google_urlpatterns)),
]


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pet.urls")),
    path("user/", include("userauth.urls")),
    path("adoption/", include("adoption.urls")),
    path("accounts/", include(social_urlpatterns)),
    # CHANGE PASSWORD
    path(
        "password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns = [] + urlpatterns
