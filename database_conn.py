import psycopg2  
import crawl_engine
import data_class_test



def db_conn(d_entry):
	conn = psycopg2.connect(database='postgres',user='postgres',password='1985712',host= '54.186.47.255',options='-c statement_timeout=100')
	cur = conn.cursor()
	isql = "INSERT INTO _odds_trend(hname,aname,hodds,aodds,result,mtime,mnumber) VALUES(%s,%s,%s,%s,%s,%s,%s);"
	ssql = "INSERT INTO DD_table(matches,ddlist) VALUES(%s,%s);"
	cur.execute(isql,(d_entry.home_name,d_entry.away_name,str(d_entry.home_odds),str(d_entry.away_odds),d_entry.result,d_entry.match_time,d_entry.match_no))
	ddlist = data_class_test.ddlist_restruct(d_entry)
	matches = d_entry.match_no
	cur.execute(ssql,(matches,ddlist))
	conn.commit()
	cur.close()
	conn.close()
	

webpage = 'http://211.151.108.43/soccer/match/742165/ah/handicap/27/'
entry = data_class_test.odds_trend()
entry = crawl_engine.capture_matchesdata(webpage)
#db_conn(entry)
