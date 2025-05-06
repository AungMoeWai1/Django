from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q

def members(request):
  # mymembers=Member.objects.all().values()

  #To filter for the specific member by using or operator  
  mydata = Member.objects.filter(firstname='Emil').values() | Member.objects.filter(firstname='Tobias').values()
  #Short format for the specific query
  mydata = Member.objects.filter(Q(firstname='Tobias') | Q(firstname='Aung')).values()

  template = loader.get_template('all_members.html')
  context={
    'mymembers':mydata,
  }
  return HttpResponse(template.render(context,request))

def details(request,id):
  mymembers=Member.objects.get(id=id)
  template=loader.get_template("details.html")
  context={
    'mymember':mymembers,
  }
  return HttpResponse(template.render(context,request))

def main(request):
  template=loader.get_template("main.html")
  return HttpResponse(template.render())

def testing(request):
  template=loader.get_template("template.html")
  context={
    'firstname': 'Linus',
    "fruits":['Apple','Banana','Coconut','Grape'],
    'greeting':1,
  }
  return HttpResponse(template.render(context,request))

def footerTest(request):
  template=loader.get_template("template.html")
  return HttpResponse(template.render())