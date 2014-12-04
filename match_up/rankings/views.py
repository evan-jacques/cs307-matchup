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
	nhl_rank = "<table><caption>Best NHL Score</caption><tr><th>Username</th><th>Points</th></tr>"
	for h in nhl:
		g = '<tr><td>%s</td><td>%s</td></tr>' % (str(h.username), str(h.score_nhl))
		nhl_rank = nhl_rank + g
	nhl_rank = nhl_rank + '</table>'
	nba_rank = "<table><caption>Best NBA Score</caption><tr><th>Username</th><th>Points</th></tr>"
	for b in nba:
		g = '<tr><td>%s</td><td>%s</td></tr>' % (str(b.username), str(b.score_nba))
		nba_rank = nba_rank + g
	nba_rank = nba_rank + '</table>'
	total_rank = "<table><caption>Best Total Score</caption><tr><th>Username</th><th>Points</th></tr>"
	for t in total:
		g = '<tr><td>%s</td><td>%s</td></tr>' % (str(t.username), str(t.score_total))
		total_rank = total_rank + g
	total_rank = total_rank + '</table>'
	return render_to_response('rankings.html',{'nhl_rank' : nhl_rank, 'nba_rank' : nba_rank, 'total_rank' : total_rank, 'users': users},context_instance=RequestContext(request))
	
