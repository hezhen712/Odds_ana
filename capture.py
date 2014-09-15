import urllib2,os,re
import urllib

crawl_url_1 = 'http://211.151.108.43/soccer/match/'
crawl_url_2 = '/ah/handicap/27/'
match_number = 718900





def capture_data(page,match_number):
        s = '/home/ubuntu/test' + str(match_number) + '.txt'
        file = open(s,'w')
        file.write(str(page))
        file.close()
	
while match_number<=718999:
        webpage = crawl_url_1+str(match_number)+crawl_url_2
        capture_web(webpage,match_number)
        match_number = match_number + 1
