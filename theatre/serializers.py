from datetime import datetime, date
from django.core.exceptions import ObjectDoesNotExist


from rest_framework import serializers
from rest_framework.fields import empty
from .models import *

import datetime
class TheatreSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Theatre



class AvailableSlotSerializer(serializers.Serializer):
    theatre_id = serializers.IntegerField(required=True)
    slot = serializers.CharField(required=False)
    day = serializers.DateField(input_formats=["%Y-%m-%d"], required=False)


class SlotSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Slot
    def save(self):

        validated_data = dict(self.validated_data)
        if validated_data['start_time'] < datetime.time(8,0,0) or \
              validated_data['end_time'] > datetime.time(20,0,0):
            raise serializers\
                   .ValidationError('showtime should be between 8 AM and 8 PM')


