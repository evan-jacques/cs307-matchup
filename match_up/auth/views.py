from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .models import UserPicks, Users, Schedule
import datetime
import pytz
import MySQLdb
import hashlib

def connect_to_db(username,password,host,database,echo=False,pool_size=20):
    print database
    db = MySQLdb.connect(host, username, password, database)
    return db.cursor(), db

def login_user(request):
    state = "Log In"
    html = "/login/"
    username = password = ''
    print request.POST
    if request.POST:

        username = request.POST.get('username')
        password = request.POST.get('password')
        

        hashedPass = hashlib.sha224(password).hexdigest()
        print hashedPass
        
        user = Users.objects.get(username = username)
        print user.password
        if user.password == hashedPass:

            
            
            print request.POST
            yyyymmdd = int(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime("%Y%m%d"))
            user = (Users.objects.filter(username = username))
            for u in user:
                users = u
            todaysGames = list(Schedule.objects.filter(game_id = yyyymmdd))
            userPicks = list(UserPicks.objects.filter(user_id = users.user_id))
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

            return render_to_response('index.html',{'html':html, 'state':state, 'username': username, 'users': users, 'TABLE':TABLE, 'todaysGames' : todaysGames, 'matches' : matches}, context_instance=RequestContext(request))

        else:
            state = "Your username and/or password were incorrect."

            return render_to_response('auth.html',{'html':html, 'state':state, 'username': username}, context_instance=RequestContext(request))
    return render_to_response('auth.html',{'html':html, 'state':state, 'username': username}, context_instance=RequestContext(request))