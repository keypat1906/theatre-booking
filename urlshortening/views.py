from django.conf import settings
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseRedirect, HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
from urlshortening.models import Url, get_short_url, generate_short_id
from .forms import LongUrlForm, ShortUrlForm


@csrf_exempt
def shortUrl(request):
    fullurl=''
    if request.method == "POST":
      urlForm = ShortUrlForm(request.POST)
      if urlForm.is_valid():
         short_id = urlForm.cleaned_data.get('url')[-6:]
         try:
             url = Url.objects.get(pk=short_id)
             if url.is_expired:
                 return HttpResponse({"error": "Link is expired", "data": ""}, status=404)
         except Url.DoesNotExist:
             return HttpResponse("short url doesn't exist", status=404)

         return render(request, 'shortUrl.html', {'full_url': url.url})

    else:
      urlForm = ShortUrlForm()
    return render(request, 'shortUrl.html', {'short_id': fullurl})


@csrf_exempt
def longUrl(request):
    short_id = ''
    if request.method == "POST":
      urlForm = LongUrlForm(request.POST)
      if urlForm.is_valid():
         full_url = urlForm.cleaned_data.get('url')
         url = get_short_url(full_url)
         return render(request, 'longUrl.html', {'full_url': url,'short_id': url.short_id})
    else:
      urlForm = LongUrlForm()
    return render(request, 'longUrl.html', {'short_id': short_id})


@csrf_exempt 
@require_POST
def get_short_link(request):
    data = json.loads(request.body)
    full_url = ''
    if 'full_url' in data:
        full_url = data['full_url']
    else:
        return JsonResponse({"error": "full_url is empty", "data": ""}, status=400)
    if len(full_url) > Url._meta.get_field("url").max_length:
        return JsonResponse({"error": "full_url is too long", "data": ""}, status=400)
    url = get_short_url(full_url)
    return JsonResponse({"error": "", "data": {
        "short_id": url.short_id,
        "short_url_path": settings.SHORT_URL_PATH
    }})


@require_GET
def get_full_link(request, short_id):
    try:
        url = Url.objects.get(pk=short_id)
        if url.is_expired:
            return JsonResponse({"error": "Link is expired", "data": ""}, status=404)
        return JsonResponse({"error": "", "data": {"full_url": url.url}})
    except Url.DoesNotExist:
        return JsonResponse({"error": "Url doesn\'t exist", "data": ""}, status=404)


