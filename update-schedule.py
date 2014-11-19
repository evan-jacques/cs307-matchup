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
	for league in ['NBA', 'NHL']:
		date = 20141118
		data = scores.today(league,date)
		print data
		for game in data:
			hteam = game['home']
			ateam = game['away']
			status = game['status']
			start = game['clock']
			hscore = int(game['home-score'])
			ascore = int(game['away-score'])
			sport = game['league']
			winner = ''
			print hscore
			if hscore > ascore:
				winner = hteam
				print 'h'
			else:
				winner = ateam
				print 'a'
			dbcursor.execute("INSERT INTO Schedule(game_id,league,time,status,home_team,home_score,away_team,away_score,winner) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE game_id = Values(game_id), home_team = Values(home_team), away_team = Values(away_team)",(date,sport,start,status,hteam,hscore,ateam,ascore,winner))
		db.commit()

