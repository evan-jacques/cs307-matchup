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

def rankings(request):
	uid = request.POST['userid']
	users = Users.objects.get(user_id = uid)
	nhl = list(Users.objects.all().order_by('-score_nhl'))
	nba = list(Users.objects.all().order_by('-score_nba'))
	total = list(Users.objects.all().order_by('-score_total'))
	counth = 1
	countb = 1
	countt = 1
	nhl_rank = "<table><caption><h1>Best NHL Score</h1></caption><tr><th>Rank</th><th>Username</th><th>Points</th></tr>"
	for h in nhl:
		if counth > 10:
			counth = 1
			break
		g = '<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (str(counth),str(h.username), str(h.score_nhl))
		counth += 1
		nhl_rank = nhl_rank + g
	nhl_rank = nhl_rank + '</table>'
	nba_rank = "<table><caption><h1>Best NBA Score</h1></caption><tr><th>Rank</th><th>Username</th><th>Points</th></tr>"
	for b in nba:
		if countb > 10:
			countb = 1
			break
		g = '<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (str(countb),str(b.username), str(b.score_nba))
		countb += 1
		nba_rank = nba_rank + g
	nba_rank = nba_rank + '</table>'
	total_rank = "<table><caption><h1>Best TOTAL Score</h1></caption><tr><th>Rank</th><th>Username</th><th>Points</th></tr>"
	for t in total:
		if countt > 10:
			countt = 1
			break
		g = '<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (str(countt),str(t.username), str(t.score_total))
		countt += 1
		total_rank = total_rank + g
	total_rank = total_rank + '</table>'
	return render_to_response('rankings.html',{'nhl_rank' : nhl_rank, 'nba_rank' : nba_rank, 'total_rank' : total_rank, 'users': users},context_instance=RequestContext(request))
	
