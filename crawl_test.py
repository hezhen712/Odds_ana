# new crawl engine
#capture data by terms
import urllib2


def get_zucailist(seed):
	webpage = 'http://211.151.108.43/zucai/' + str(seed) +'/'
	page1 = urllib2.urlopen(webpage)
	pages = page1.read()
	fcont = '/soccer/match/'
	fpot = pages.find(fcont)
	mlist = []
	while fpot != -1:
		mlist.append(pages[fpot+14:fpot+20])
		fpot = pages.find(fcont,fpot+1)
	return mlist