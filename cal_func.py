import HTMLParser
import urllib2,sys,ast

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

url = 'http://211.151.108.43/soccer/match/714926/ah/handicap/27/'
page1 = urllib2.urlopen(url,timeout = 3)
pages = page1.read()
list1 = pages[pages.find('data1=')+6:pages.find(';',pages.find('data1='))]
list1 = ast.literal_eval(list1)
list2 = pages[pages.find('data2=')+6:pages.find(';',pages.find('data2='))]
list2 = ast.literal_eval(list2)
str1 = pages[pages.find('homeName')+11:pages.find(';',pages.find('homeName'))-1]
str2 = pages[pages.find('awayName')+11:pages.find(';',pages.find('awayName'))-1]
