# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpRequest
# from .models import UserPicks, Users, Schedule
import MySQLdb


def confirm(request):
	print request.POST
	return render_to_response('confirm.html')
