from rest_framework import viewsets, status, mixins, filters
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from . import serializers
from . import models
from . import utils

class BaseViewSet(viewsets.ReadOnlyModelViewSet, mixins.UpdateModelMixin,
                  mixins.CreateModelMixin):
    pass


class TheatreViewSet(BaseViewSet):
    serializer_class = serializers.TheatreSerializer
    queryset = models.Theatre.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('theatre_id',)

    @detail_route(methods=['get'])
    def available_slots(self, request, pk=None):
       data = dict(request.query_params.items())
       instance = self.get_object()
       if 'day' in data:
           slots = models.Slot.objects.filter(slot_date=data['day']).filter(theatre=instance)
           get_avail_slots = utils.get_avail_slots(slots)
       else:
           return Response("provide the date", status=status.HTTP_400_BAD_REQUEST)
       return Response(get_avail_slots)

    
class SlotViewSet(BaseViewSet):
    serializer_class = serializers.SlotSerializer
    queryset = models.Slot.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('theatre_id','slot_date','start_time','end_time')

@api_view(['GET'])
def getslotlist(request, *args, **kwargs):
       get_avail_slots=[]
       start_time = request.GET.get('start_time')
       end_time = request.GET.get('end_time')
       slot_date = request.GET.get('slot_date')
       if start_time and end_time and slot_date:
           slots = models.Slot.objects.filter(slot_date=slot_date)
           get_avail_slots = utils.get_theatre_slots(slots,start_time,end_time)
           print("get_avail_slots",get_avail_slots)
       return Response(get_avail_slots)

    
