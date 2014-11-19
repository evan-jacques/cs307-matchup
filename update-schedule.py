import datetime
import pytz
import MySQLdb
import score_scraper as scores
import json

host = 'mysql.cs.mcgill.ca'
username = "tayre"
database = '2014fall307tayre'
password = '260480603'

def connect_to_db(username,password,host,database,echo=False,pool_size=20):
	print database
	db = MySQLdb.connect(host, username, password, database)
	return db.cursor(), db

if __name__ == '__main__':
	dbcursor, db = connect_to_db(username,password,host,database)
	date = int(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime("%Y%m%d"))
	for day in range(date-5,date + 5):
		for league in ['NBA', 'NHL']:
			data = scores.today(league,day)
			print data
			for game in data:
				hteam = game['home']
				ateam = game['away']
				status = game['status']
				start = game['clock']
				hscore = game['home-score']
				ascore = game['away-score']
				sport = game['league']
				winner = ''
				try:
					h = int(hscore)
					a = int(ascore)
					if h > a:
						winner = hteam
						print 'h'
					else:
						winner = ateam
						print 'a'
				except ValueError:
					pass
				dbcursor.execute("INSERT INTO Schedule(game_id,league,time,status,home_team,home_score,away_team,away_score,winner) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE status = Values(status), home_score = Values(home_score), away_score = Values(away_score), winner = Values(winner)",(day,sport,start,status,hteam,hscore,ateam,ascore,winner))
			db.commit()

