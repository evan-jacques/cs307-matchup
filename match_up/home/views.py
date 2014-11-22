# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Users


		

def index(request):
	users = Users(username = "user1")
	
	

	return render_to_response('index.html', {'users': users})

	# , context_instance=RequestContext(request)