from django.conf.urls import url, include
from django.conf import settings                                 
from . import views
from .routers import CustomRouter
router = CustomRouter()
router.register('theatre', views.TheatreViewSet, base_name='theatreiewset')
router.register('slot', views.SlotViewSet, base_name='slotviewset')

urlpatterns = [ 
        url(r'', include(router.urls)),
        url(r'slotlist/$',views.getslotlist, name='slotlist')
]
