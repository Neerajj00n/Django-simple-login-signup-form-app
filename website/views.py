from django.shortcuts import render
from django.http import HttpResponse
from website.models import Data
from django.template import RequestContext
import hashlib
# Create your views here.

def home(request):
	if  "first" in request.POST and "last" in request.POST and  "email" in request.POST and "mobile" in request.POST and "password" in request.POST and "password2" in request.POST:

		Firstname = request.POST["first"]
		Lastname = request.POST["last"]
		Email =  request.POST["email"]
		Mobile = request.POST["mobile"]
		Password = request.POST["password"]
		Password2 = request.POST["password2"]
	
	
		try:    
			if Password2 != Password:
                                return HttpResponse("Password didn't match")
			elif Data.objects.get(email = Email):
                        	return HttpResponse("email address is allready exist")

#			if Password2 != Password:
#               			return HttpResponse("Password didn't match")

		except:
			hashing = hashlib.md5(Password) #encrypting password
	                key = hashing.hexdigest()
		
			Data.objects.create(firstname = Firstname, lastname = Lastname, email = Email , mobile = Mobile , password = key) #saving data in database
			
			return HttpResponse('Account succesfully Created <a href="/">Login Now</a>')



	return HttpResponse(render(request, "index.html", {}))


def login(request):
	
	if "email" in request.POST and "password" in request.POST:
	
		Email = request.POST["email"]
		Password = request.POST["password"]

		hashing = hashlib.md5(Password) #encrypting password
                key = hashing.hexdigest()	

	try:    
		get = Data.objects.get(email = Email , password = key) #matching data from database
		return HttpResponse(render(request, "main.html", {}))

	except:
		get = False
		return HttpResponse("Login fail, incorrect Email address or Password")
	
def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response	
