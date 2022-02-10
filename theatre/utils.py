import datetime
from . import models

def get_theatre_slots(slots,start_time,end_time):
   slots_dit = {}
   prevend=datetime.time(1,1,1)
   tid=[]
   theatres_all = models.Theatre.objects.all().values('theatre_id')
 
   for t in theatres_all:
          tid.append(t['theatre_id'])
   print("theatres are ",tid)
  
   if slots.count() == 0:
       return tid
   for slot in slots.values():
       if slot['theatre_id'] in tid:
           tid.remove(slot['theatre_id'])

   print("updated theatres are ",tid)

   print ("slots are ",slots.values())
   for slot in slots.values():
       if slot['theatre_id'] in slots_dit:
           slots_dit[slot['theatre_id']].append([slot['start_time'],slot['end_time']])
       else:
           slots_dit[slot['theatre_id']] = [slot['start_time'],slot['end_time']]
   print("slot dit",slots_dit)

   for theatre, slots in slots_dit.items():
           if slots[0] >= datetime.datetime.strptime(end_time, '%H-%M-%S').time():
               #and slot_end <= datetime.datetime.strptime(end_time, '%H-%M-%S').time():
               tid.append(theatre)
               break
           #prevend = slot
   return tid

def get_avail_slots(slots):

   start =''
   slots = slots.values()
   slottime=[]
   availtime=[]  
   prev=datetime.time(1,1,1)
   for slot in slots:
       slottime.append([slot['start_time'],slot['end_time']])
   print("slottime",slottime)

   if len(slottime) == 0:
       return [datetime.time(8,0,0),datetime.time(20,0,0)]

   if slottime[0][0] > datetime.time(8,0,0):
       availtime.append([datetime.time(8,0,0),slottime[0][0]])

   for start, end in  slottime:
       if prev < start:
          diff = [prev, start]
          availtime.append(diff)
       prev = end

   availtime.append([end,datetime.time(20,0,0)])
   print ("avail slots are ", availtime)
   return availtime
   
