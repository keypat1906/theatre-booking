from django.conf.urls import url
from django.conf import settings

from urlshortening.views import get_full_link, get_short_link, longUrl, shortUrl

urlpatterns = [
    url(r'^expand/(?P<short_id>.+)/$', get_full_link),
    url(r'^short/$', get_short_link),
    url(r'^fullurl/', longUrl, name='longUrl'),
    url(r'^shorturl/', shortUrl, name='shortUrl')

]
