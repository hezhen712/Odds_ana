import urllib2,os,re
import urllib

crawl_url_1 = 'http://211.151.108.43/soccer/match/'
crawl_url_2 = '/ah/line/27/'
match_number = 718900

def capture_web(url):
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	page = response.read()
	capture_data(page)
	
	

def capture_data(page):
	file = open('c:/test1.txt','r+')
	file.write(str(page))
	file.close()
	
	

while match_number<=718999:
	webpage = crawl_url_1+str(match_number)+crawl_url_2
	capture_web(webpage)
	match_number = match_number + 1
	
	