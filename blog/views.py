from django.shortcuts import render
from . models import Home
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import HomeForm
def home_list(request):
  homes = Home.objects.all()
  print("website")
  return render(request, 'blog/home_list.html',{'homes': homes})
@csrf_exempt
def output(request):
  if request.method == "POST":
    form=(request.POST)
    print(f"form:{form}")
    data=form.dict()
    firstname= data["firstname"]
    lastname=data["lastname"]
    latitude=data["latitude"]
    longitude=data["longitude"]
    # output = encryption(latitude,longitude)
    output={"secret":"abcdefghi"}
    print(f"output:{output}")
    # body = json.loads(request.body)
    # print (request.json())
    # print(f"body:{body}")
    return render(request, 'blog/output.html',output)
def encryption(latitude,longitude):
    # latitude=input('Enter the Latitude')
    # longitude=input('Enter Longitude:')
    message=str(latitude+longitude)
    alphabet="abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    # key = input("Enter a encrypt key of your Choice (at lease 8 Numbers long): ")
    key="5"
    encrypt =''
    for i in message:
      position=alphabet.find(i)
      newposition=(position+ int(key) )%94
      encrypt+=alphabet [newposition]
    output = (encrypt)
    print ('Encrypted Message')
    return output






