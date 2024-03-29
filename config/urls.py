
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from home.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path("users/", include("users.urls")),
    path("cart/", include("cart.urls")),
    path("fact/", include("send_invoice.urls"))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)