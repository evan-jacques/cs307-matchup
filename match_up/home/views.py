# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.forms.formsets import formset_factory

from .models import UserPicks, Users, Schedule
import datetime
import pytz
from .forms import tableForm

def index(request):
	# TABLE = "<table>"
	# for game in todaysGames 
	yyyymmdd = int(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime("%Y%m%d"))
	users = Users(username = "user1")
	todaysGames = list(Schedule.objects.filter(game_id = yyyymmdd))
	#return render_to_response('index.html', {'users': users, 'todaysGames' : todaysGames})
	# tableFormSet = formset_factory(tableForm, extra = (len(todaysGames)-1) )
	# formset = tableFormSet()

	#TABLE = "<table>"
	# if request.method == 'GET':
	
	matches = []
	for game in todaysGames:
		match = []
		match.append(game.home_team)
		match.append(game.away_team)
		match.append(game.time)
		match.append(game.league)
		matches.append(match)
	return render_to_response('index.html', {'users': users, 'todaysGames' : todaysGames, 'matches' : matches})


		
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


'''
		g = "<form><tr> <td> %s </td><td><input=\"radio\" name=\"pick %s %s %s %s\" value=\"%s %s %s\"> </td> <td>%s</td><td> %s </td> <td> <input= \"radio\" name=\"pick %s %s %s %s\" value=\"%s %s %s\"></td><td>%s</td> </tr> </form>"  % (str(game.league), str(game.game_id), str(game.league), str(game.home_team), str(game.away_team), str(game.game_id), str(game.league), str(game.home_team), str(game.home_team), str(game.away_team), str(game.game_id), str(game.league), str(game.home_team), str(game.away_team),  str(game.game_id), str(game.league), str(game.away_team),str(game.time))
		TABLE = TABLE + g
	TABLE = TABLE + "</table>"
# game_id = "yyyymmdd"
'''

	#return render_to_response('index.html', {'users': users, 'todaysGames' : todaysGames, 'matches' : matches})

	# , context_instance=RequestContext(request)
