import HTMLParser
import urllib2,sys

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




ct = open('c:/users/ssimah/downloads/1211221.htm','r+')
content = ct.read()
a = content.find('ah_line_table01')
b = content.find('/table',a)
p = TableParser()
p.feed(content[a:b])
p.get_result()
