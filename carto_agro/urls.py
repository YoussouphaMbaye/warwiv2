"""carto_agro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url

from django.conf import settings

from django.views.static import serve


from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage


from django.contrib import admin
from django.urls import path,include
#from django.conf import settings
from django.conf.urls.static import static
from app.admin import admin_site

urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),

    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

    path('admin/', admin_site.urls),
    path('', include('app.urls')),
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("assets/mesimages/logo_warwi.png")),
    ),
    
 ]
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# #print(staticfiles_storage.url(''))
# if settings.DEBUG:
#     urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





