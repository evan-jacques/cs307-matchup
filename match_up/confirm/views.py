# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpRequest
from .models import UserPicks, Users, Schedule
import MySQLdb

host = 'mysql.cs.mcgill.ca'
username = "tayre"
database = '2014fall307tayre'
password = '260480603'

def connect_to_db(username,password,host,database,echo=False,pool_size=20):
	print database
	db = MySQLdb.connect(host, username, password, database)
	return db.cursor(), db

def confirm(request):
	dbcursor, db = connect_to_db(username,password,host,database)
	picks = []
	for p in request.POST:
		picks.append(request.POST[p])
	print picks
	for pick in picks:
		try:
			data = pick.split(',')
			date = data[0]
			league = data[1]
			home_team = data[2]
			away_team = data[3]
			user_pick = data[4]
			u_id = data[5]
			_id = 0
			winner = ''
			points = 0
			dbcursor.execute("INSERT INTO User_picks(id, user_id, game_id, league, home_team, away_team, user_pick, winner, points) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE user_pick = Values(user_pick), winner = Values(winner), points = Values(points)", (_id, u_id, date, league, home_team, away_team, user_pick, winner, points))
		except IndexError:
			continue
	uid = request.POST['userid']
	print uid
	user = (Users.objects.filter(user_id = str(uid)))
	users = ''
	for u in user:
		users = u
	print users
	history = list(UserPicks.objects.filter(user_id = uid))
	TABLE = "<table><tr><th>Game Date</th><th>League</th><th>Home</th><th>Away</th><th>Your Pick</th><th>Winning Team</th><th>Points</th></tr>"
	for game in history:
		g = '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (str(game.game_id), str(game.league), str(game.home_team), str(game.away_team), str(game.user_pick), str(game.winner), str(game.points))
		TABLE = TABLE + g
	TABLE = TABLE + '</table>'


	return render_to_response('confirm.html',{'TABLE': TABLE, 'users': users},context_instance=RequestContext(request))
