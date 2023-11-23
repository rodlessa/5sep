from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  top5 = Member.objects.all().order_by("-kilos")[:5]
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
    'top5' : top5,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))