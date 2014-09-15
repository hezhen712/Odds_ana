import HTMLParser
import urllib2,sys
import data_class_test
import ast,socket

class TableParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.in_td = False
	self.data = []
    
    def handle_starttag(self, tag, attrs):
        if tag == 'td' or tag == 'p':
            self.in_td = True
    
    def handle_data(self, data):
        if self.in_td:
	    self.data += data
    
    def get_result(self):
	return self.data
    
    def handle_endtag(self, tag):
        self.in_td = False


class SpanParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.in_td = False
	self.data = []
    
    def handle_starttag(self, tag, attrs):
        if tag == 'span':
            self.in_td = True
    
    def handle_data(self, data):
        if self.in_td:
	    self.data += data
    
    def get_result(self):
	return self.data
    
    def handle_endtag(self, tag):
        self.in_td = False

class PParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.in_td = False
	self.data = []
    
    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.in_td = True
    
    def handle_data(self, data):
        if self.in_td:
	    self.data += data
    
    def get_result(self):
	return self.data
    
    def handle_endtag(self, tag):
        self.in_td = False
		
		
def capture_matchesdata(pageurl):
	
	page1 = urllib2.urlopen(pageurl,timeout = 300)
	pages1 = page1.read()
	page2 = urllib2.urlopen(pageurl[:-12],timeout = 3)
	pages2 = page2.read()
	mnumber = pageurl[35:41]
	#except socket.timeout, e:
	#	raise capture_matchesdata("there is a error:%r" % e)
	#	pass
	if if_datas_(pages1):
		st = pages2.find('matchTeam')
		ed = pages2.find('table',st)
		pages3 = pages2[st:ed]
		pages4 = pages2[st-300:st-185]
		list1 = pages1[pages1.find('data1=')+6:pages1.find(';',pages1.find('data1='))]
		list1 = ast.literal_eval(list1)
		list2 = pages1[pages1.find('data2=')+6:pages1.find(';',pages1.find('data2='))]
		list2 = ast.literal_eval(list2)
		str1 = pages1[pages1.find('homeName')+10:pages1.find(';',pages1.find('homeName'))-1]
		str2 = pages1[pages1.find('awayName')+10:pages1.find(';',pages1.find('awayName'))-1]
		cstr1 = str1.decode('GBK').encode('utf-8')
		cstr2 = str2.decode('GBK').encode('utf-8')
		res_page = SpanParser()
		res_page.feed(pages3)
		res = res_page.get_result()
		if len(res) == 2:
			ress = '%s:%s' % (res[0],res[1])
		else:
			ress = 'no scores'
		time_page = PParser()
		time_page.feed(pages4)
		time = ''.join(time_page.get_result())
		_particular_match_ = data_class_test.odds_trend()
		_particular_match_._init_(list1,list2,cstr1,cstr2,ress,time,mnumber)
		return _particular_match_
		page1.close()
		page2.close()
	
	



def if_datas_(pages):
	if pages.find('data1') and pages.find('data2'):
		return True
	return False
	
	
url = 'http://211.151.108.43/soccer/match/714926/ah/handicap/27/'
#capture_matchesdata(url)
	
def get_zucai(seed):
	webpage = 'http://211.151.108.43/zucai/' + str(seed) +'/'
	page1 = urllib2.urlopen(webpage,timeout= 300)
	pages = page1.read()
	fcont = '/soccer/match/'
	fpot = pages.find(fcont)
	mlist = []
	while fpot != -1:
		mlist.append(pages[fpot+14:fpot+20])
		fpot = pages.find(fcont,fpot+1)
	return mlist[::2]
	page1.close()


def now_ddlist(seed):
	crawl_url_1 = 'http://211.151.108.43/soccer/match/'
	crawl_url_2 = '/ah/handicap/27/'
	webpage = crawl_url_1 + str(seed) + crawl_url_2
	page1 = urllib2.urlopen(webpage,timeout = 300)
	pages1 = page1.read()
	page1.close()
	list1 = pages1[pages1.find('data1=')+6:pages1.find(';',pages1.find('data1='))]
	list1 = ast.literal_eval(list1)
	list2 = pages1[pages1.find('data2=')+6:pages1.find(';',pages1.find('data2='))]
	list2 = ast.literal_eval(list2)
	ddhlist = []
	ddalist = []
	for i in list1:
		new = float(i[0]) + float(i[1])
		ddhlist.append(round(new,2))
	for j in list2:
		news = float(j[0])+ float(j[1])
		ddalist.append(round(news,2))
	ddlist = ddhlist + ddalist
	return ddlist