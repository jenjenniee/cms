
from django.contrib import admin
from django.urls import path, include
from cms import views
from qna.views import base_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  include('cms.urls')),
    path('cms/', include('cms.urls')),
    path('commute/', include('commute.urls')),
    path('common/', include('common.urls')),
    path('board/', include('board.urls')),
    path('qna/', include('qna.urls')),
    path('api/', include('api.urls')),
    path('qna/', base_views.index, name='index'),  # '/' 에 해당되는 path
    path('document/', include('document.urls')),
    path('notice/', include('notice.urls'))

]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
