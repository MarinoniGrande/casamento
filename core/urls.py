from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, re_path
from django.views.decorators.csrf import csrf_exempt
import core.views

urlpatterns = [
                  re_path(r'^presentes$', csrf_exempt(core.views.ProdutosView.as_view()), name="produtos"),
                  re_path(r'^confirmacao$', csrf_exempt(core.views.ProdutosConfirmarView.as_view()), name="confirmar"),
                  re_path(r'^rsvp$', csrf_exempt(core.views.RSVPView.as_view()), name="rsvp"),
                  re_path(r'^$', core.views.HomeView.as_view(), name="home"),
              ] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
