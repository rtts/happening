from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from festival.views import *

urlpatterns = [
    url(r'^$', homepage),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_title = 'The Happening CMS'
admin.site.site_header = 'The Happening CMS'
admin.site.site_url = None
admin.site.index_title = 'Overzicht'

