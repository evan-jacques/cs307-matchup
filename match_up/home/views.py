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
	yyyymmdd = int(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime("%Y%m%d"))
	users = Users(username = "user1")
	todaysGames = list(Schedule.objects.filter(game_id = yyyymmdd))
	userPicks = list(UserPicks.objects.filter(user_id = users.user_id))
	#return render_to_response('index.html', {'users': users, 'todaysGames' : todaysGames})
	# tableFormSet = formset_factory(tableForm, extra = (len(todaysGames)-1) )
	# formset = tableFormSet()

	TABLE = "<table>"
	# if request.method == 'GET':
	
	matches = []
	for game in todaysGames:
		match = []
		match.append(game.game_id)
		match.append(game.home_team)
		match.append(game.away_team)
		match.append(game.time)
		match.append(game.league)
		matches.append(match)

		dbcursor, db = connect_to_db(username,password,host,database)
		for pick in userPicks:
			_id = 0
			_points = 0
			nhl_points = 0
			nba_points = 0
			if (str(game.home_team) == str(pick.home_team) and str(game.away_team) == str(pick.away_team)):
				if (game.winner == pick.user_pick):
					#add a point to the user_pick
					_points = 1

					if (game.league == "NHL"):
						nhl_points += 1
					else:
						nba_points += 1



				dbcursor.execute("INSERT INTO User_Picks(id, user_id, game_id, league, home_team, away_team, user_pick, winner, points) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE winner = Values(winner), points = Values(points)", (_id, pick.user_id, pick.game_id, pick.league, pick.home_team, pick.away_team, pick.user_pick, game.winner, _points))
			total_points = nhl_points + nba_points
			dbcursor.execute("INSERT INTO Users(id, user_id, username, email, password, score_total, score_nhl, score_nba) VALUES(%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE score_total = Values(score_total), score_nhl = Values(score_nhl), score_nba = Values(score_nba)", (_id, users.user_id, users.username, users.email, users.password, total_points, nhl_points, nba_points))
	

		g = "<tr> <td> %s </td><td><input type=\"radio\" name=\"pick%s%s%s%s\" value=\"%s%s%s\">%s</td><td><input type=\"radio\" name=\"pick%s%s%s%s\" value=\"%s%s%s\">%s</td><td>%s</td> </tr>"  % (str(game.league), str(game.game_id), str(game.league), str(game.home_team), str(game.away_team), str(game.game_id), str(game.league), str(game.home_team), str(game.home_team),  str(game.game_id), str(game.league), str(game.home_team), str(game.away_team),  str(game.game_id), str(game.league), str(game.away_team), str(game.away_team), str(game.time))
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
