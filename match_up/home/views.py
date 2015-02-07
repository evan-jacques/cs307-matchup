# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.forms.formsets import formset_factory

from .models import UserPicks, Users, Schedule
import datetime
import pytz
from .forms import tableForm
import MySQLdb


host = 'mysql.cs.mcgill.ca'
username = "tayre"
database = '2014fall307tayre'
password = '260480603'
def connect_to_db(username,password,host,database,echo=False,pool_size=20):

	db = MySQLdb.connect(host, username, password, database)
	return db.cursor(), db

def index(request):
	
	userN = ''
	userN = request.POST.get('username') 

	yyyymmdd = int(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime("%Y%m%d"))

	user = (Users.objects.filter(username = userN))
	for u in user:
		users = u

	todaysGames = list(Schedule.objects.filter(game_id = yyyymmdd))

	userPicks = list(UserPicks.objects.filter(user_id = users.user_id))
	

	TABLE = "<table><tr><th>League</th><th>Home</th><th>Away</th><th>Start Time</th>"
	
	matches = []
	for game in todaysGames:
		g = "<tr> <td> %s </td><td><input type=\"radio\" name=\"pick%s%s%s%s\" value=\"%s,%s,%s,%s,%s,%s\">%s</td><td><input type=\"radio\" name=\"pick%s%s%s%s\" value=\"%s,%s,%s,%s,%s,%s\">%s</td><td>%s</td> </tr>"  % (str(game.league), str(game.game_id), str(game.league), str(game.home_team), str(game.away_team), str(game.game_id), str(game.league),str(game.home_team), str(game.away_team), str(game.home_team), str(users.user_id), str(game.home_team),  str(game.game_id), str(game.league), str(game.home_team), str(game.away_team), str(game.game_id), str(game.league), str(game.home_team), str(game.away_team),str(game.away_team), str(users.user_id), str(game.away_team), str(game.time))
		TABLE = TABLE + g
	TABLE = TABLE + "</table>"
		return render_to_response('index.html', {'TABLE': TABLE, 'users': users, 'todaysGames' : todaysGames, 'matches' : matches},context_instance=RequestContext(request))


