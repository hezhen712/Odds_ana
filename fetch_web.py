import crawl_engine
import sys,database_conn,data_class_test
import sys,os,re
import urllib2,psycopg2

def fetch_test1(match_number):
	crawl_url_1 = 'http://211.151.108.43/soccer/match/'
	crawl_url_2 = '/ah/handicap/27/'
	webpage = crawl_url_1 + str(match_number) + crawl_url_2
	entry = data_class_test.odds_trend()
	entry = crawl_engine.capture_matchesdata(webpage)
	database_conn.db_conn(entry)
		
	
		
		
def fetch_test2():
	crawl_url_1 = 'http://211.151.108.43/soccer/match/'
	crawl_url_2 = '/ah/handicap/27/'
	match_number = 718000
	while match_number<=718599:
		webpage = crawl_url_1 + str(match_number) + crawl_url_2
		entry = data_class_test.odds_trend()
		entry = crawl_engine.capture_matchesdata(webpage)
		database_conn.db_conn(entry)
		match_number = match_number + 1
	

def fetch_byterm(seed):
	crawl_url_1 = 'http://211.151.108.43/soccer/match/'
	crawl_url_2 = '/ah/handicap/27/'
	mlist = crawl_engine.get_zucai(seed)
	for i in mlist:
		webpage = crawl_url_1 + i + crawl_url_2
		entry = data_class_test.odds_trend()
		entry = crawl_engine.capture_matchesdata(webpage)
		database_conn.db_conn(entry)
	
