from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, re_path
from django.views.decorators.csrf import csrf_exempt
import core.views

urlpatterns = [
                  re_path(r'^presentes$', core.views.ProdutosView.as_view(), name="produtos"),
                  re_path(r'^confirmar$', core.views.ProdutosView.as_view(), name="confirmar"),
                  re_path(r'^$', core.views.HomeView.as_view(), name="home"),
              ] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static('workspace/' + settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
