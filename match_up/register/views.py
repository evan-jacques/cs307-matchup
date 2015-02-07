# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .models import Users
import MySQLdb
import hashlib

host = 'mysql.cs.mcgill.ca'
username = "tayre"
database = '2014fall307tayre'
password = '260480603'
def connect_to_db(username,password,host,database,echo=False,pool_size=20):
	
	db = MySQLdb.connect(host, username, password, database)
	return db.cursor(), db

def register(request):
	user = email = passw = ''

	if request.POST:

		user = request.POST.get('username')
		email = request.POST.get('email')
		passw = request.POST.get('password')
		registered = "<h3>Here's your information (Protip: Write it down! We don't hold on to your password in plaintext)</h3><p>Username:%s</p><p>Password:%s</p><p>Go back to the login and sign in now!</p>"%(str(user), str(passw))


		if (user and email and passw != ''):
			hashedPass = hashlib.sha224(passw).hexdigest()
			# Need better way to make a user ID
			u_id = ord(user[0])*ord(user[0])+ord(user[0])*ord(user[0])*len(user)

			if not(Users.objects.exists()):
				registered = "<h3><span style=\"color:red;\">That name username is already in use, go to the login in page and try another!</span></h3>"
				return render_to_response('register.html', {'registered': registered})
			else:
				
				newuser = Users.objects.create(id = u_id, user_id = u_id, username = user, email = email, password = hashedPass, score_total = 0, score_nba = 0, score_nhl = 0)

				return render_to_response('register.html', {'registered': registered })

		else:
			registered = "<h3><span style=\"color:red;\">It seems you didn't fill out the you the information field properly return the login and try again</span> </h3>"

			return render_to_response('register.html', {'registered': registered})
