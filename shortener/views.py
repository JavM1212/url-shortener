from django.shortcuts import render, redirect
from django.http import HttpResponse
import uuid

from .models import Url

# Create your views here.

def index(request):
  return render(request, 'index.html')

def create(request):
  if request.method == 'POST':
    link = request.POST['link']
    uid = str(uuid.uuid4())[:5]
    new_url = Url(link = link, uuid = uid)
    new_url.save()
    return HttpResponse(uid)

def go(request, pk):
  url_details = Url.objects.get(uuid=pk)

  arr = []
  https = 'h'

  for i in url_details.link:
    arr.append(i)

  string = "".join(arr[0])

  if string in https:
    return redirect(url_details.link)
  elif i not in https:
    return redirect('https://' + url_details.link)