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
	print database
	db = MySQLdb.connect(host, username, password, database)
	return db.cursor(), db

def index(request):
	# TABLE = "<table>"
	# for game in todaysGames
	userN = ''
	userN = request.POST.get('username') 
	print request.POST
	yyyymmdd = int(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime("%Y%m%d"))

	user = (Users.objects.filter(username = userN))
	for u in user:
		users = u

	todaysGames = list(Schedule.objects.filter(game_id = yyyymmdd))

	userPicks = list(UserPicks.objects.filter(user_id = user.user_id))
	#return render_to_response('index.html', {'users': users, 'todaysGames' : todaysGames})
	# tableFormSet = formset_factory(tableForm, extra = (len(todaysGames)-1) )
	# formset = tableFormSet()

	TABLE = "<table><tr><th>League</th><th>Home</th><th>Away</th><th>Start Time</th>"
	# if request.method == 'GET':
	
	matches = []
	for game in todaysGames:
		g = "<tr> <td> %s </td><td><input type=\"radio\" name=\"pick%s%s%s%s\" value=\"%s,%s,%s,%s,%s,%s\">%s</td><td><input type=\"radio\" name=\"pick%s%s%s%s\" value=\"%s,%s,%s,%s,%s,%s\">%s</td><td>%s</td> </tr>"  % (str(game.league), str(game.game_id), str(game.league), str(game.home_team), str(game.away_team), str(game.game_id), str(game.league),str(game.home_team), str(game.away_team), str(game.home_team), str(users.user_id), str(game.home_team),  str(game.game_id), str(game.league), str(game.home_team), str(game.away_team), str(game.game_id), str(game.league), str(game.home_team), str(game.away_team),str(game.away_team), str(users.user_id), str(game.away_team), str(game.time))
		TABLE = TABLE + g
	TABLE = TABLE + "</table>"
		# game_id = "yyyymmdd"
		# <input=\"radio\" name=\"pick %s %s %s %s\" value=\"%s %s %s\">%s
	# str(game.game_id), str(game.league), str(game.home_team), str(game.away_team), str(game.game_id), str(game.league), str(game.home_team), str(game.home_team),
	# g = "<input type=\"radio\" name=\"sex\" value=\"male\">Male<br><input type=\"radio\" name=\"sex\" value=\"female\">Female"
	return render_to_response('index.html', {'TABLE': TABLE, 'users': users, 'todaysGames' : todaysGames, 'matches' : matches},context_instance=RequestContext(request))


		
			# form = tableForm(request.GET)

			# if form.is_valid():
			# 	print "1"
			# 	cd = form.cleaned_data
			# 	user_picks.objects.create(pick=cd['pick'] )
			# 	print form
			# else:
			# 	print "not 1"
			# 	form = tableForm()

			# 	print form


		



	#return render_to_response('index.html', {'users': users, 'todaysGames' : todaysGames, 'matches' : matches})

	# , context_instance=RequestContext(request)
