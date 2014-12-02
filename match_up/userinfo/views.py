# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .models import Users
import MySQLdb

def information(request):
	


	#some tests
	userN = 'trevor'


	user = Users.objects.get(username = userN)

	TABLE = "<table> <tr><td>Total Points</td><td>%s</td></tr> <tr><td>NHL Points</td><td>%s</td></tr> <tr><td>NBA Points</td><td>%s</td></tr>" % (str(user.score_total), str(user.score_nhl), str(user.score_nba))
	TABLE = TABLE +	"</table>"


	return render_to_response('userinfo.html', {'user' : user, 'TABLE' : TABLE})
