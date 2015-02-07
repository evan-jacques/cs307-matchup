import datetime
import pytz
import MySQLdb

host = 'mysql.cs.mcgill.ca'
username = "tayre"
database = '2014fall307tayre'
password = '260480603'
def connect_to_db(username,password,host,database,echo=False,pool_size=20):
	print database
	db = MySQLdb.connect(host, username, password, database)
	return db.cursor(), db
def update_points():
	yyyymmdd = int(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime("%Y%m%d"))
	dbcursor, db = connect_to_db(username,password,host,database)
	results = []
	for day in range(yyyymmdd - 2, yyyymmdd + 1):
		dbcursor.execute('SELECT * FROM Schedule WHERE game_id = %s' % str(day))
		for r in dbcursor.fetchall():
			print r
			dbcursor.execute('Select * FROM User_picks WHERE game_id = %s AND home_team = %s AND away_team = %s', (str(r[1]),r[5], r[7]))
			for u in dbcursor.fetchall():
				if r[9] == u[6]:
					print str(r[9]) + ' ' + str(u[6])
					dbcursor.execute("UPDATE User_picks SET winner = %s, home_score = %s, away_score = %s, points = %s WHERE game_id = %s AND home_team = %s AND away_team = %s", (r[9], str(r[6]), str(r[8]),'1',str(r[1]),r[5], r[7]))
				else:
					print 'here'
					dbcursor.execute("UPDATE User_picks SET winner = %s, home_score = %s, away_score = %s, points = %s WHERE game_id = %s AND home_team = %s AND away_team = %s", (r[9],str(r[6]), str(r[8]),'0',str(r[1]),r[5], r[7]))
	dbcursor.execute('Select user_id From Users')
	for u_id in dbcursor.fetchall():
		nba_count = dbcursor.execute('Select * from User_picks WHERE user_id = %s AND league = "NBA" AND points = "1"' % str(u_id[0]))
		nhl_count = dbcursor.execute('Select * from User_picks WHERE user_id = %s AND league = "NHL" AND points = "1"' % str(u_id[0]))
		total_count = nba_count + nhl_count
		dbcursor.execute("UPDATE Users SET score_nhl = %s, score_nba = %s, score_total = %s WHERE user_id = %s", (str(nhl_count),str(nba_count),str(total_count), str(u_id[0])))
		db.commit()
#update_points()

