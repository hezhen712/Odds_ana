import HTMLParser
import urllib2,sys
import data_class_test
import ast,socket
from bs4 import BeautifulSoup #a module for capture webpage's content
import psycopg2  


url = 'http://211.151.108.43/soccer/match/752758/exchanges/'

def get_bifa(mn):
	webpage = 'http://211.151.108.43/soccer/match/' + str(mn) +'/exchanges/'
	page1 = urllib2.urlopen(webpage,timeout= 3000)
	pages = page1.read()
	page1.close()
	st = pages.find('compute')
	pages = pages[st+48:st+1200]
	soup = BeautifulSoup(pages,from_encoding="gb18030")
	bf = soup.find_all('td','zsObj')
	bflist = []
	for i in bf:
		bflist.append(int(i.get_text()))
	return bflist

def db_insert_bf(mn,bflist):
	conn = psycopg2.connect(database='postgres',user='postgres',password='1985712',host= '54.186.47.255',options='-c statement_timeout=100')
	cur = conn.cursor()
	gsql = "update dd_table set bifa = %s where matches = %s;"
	cur.execute(gsql,(bflist,mn))
	conn.commit()
	cur.close()
	conn.close()

def mnumber_list():
	conn = psycopg2.connect(database='postgres',user='postgres',password='1985712',host= '54.186.47.255',options='-c statement_timeout=10000')
	cur = conn.cursor()
	gsql = "Select mnumber from _odds_trend"
	cur.execute(gsql)
	mlist = cur.fetchall()
	cur.close()
	conn.close()
	m_list =[]
	for i in mlist:
		m_list.append(str(i)[2:-3])
	return m_list
	
def bifa_dbupdate():
	m_list = mnumber_list()
	for i in m_list:
		bflist = get_bifa(i)
		db_insert_bf(i,bflist)
	
def bifalst_dbupdate(mlist):
	for i in m_list:
		bflist = get_bifa(i)
		db_insert_bf(i,bflist)

def get_allresult():
	conn = psycopg2.connect(database='postgres',user='postgres',password='1985712',host= '54.186.47.255',options='-c statement_timeout=50000')
	cur = conn.cursor()
	cur.execute("select mnumber,result from _odds_trend order by mnumber;")
	mres = cur.fetchall()
	cur.close()
	conn.close()
	mr_dic = {}
	for i in mres:
		mr_dic.update({list(i)[0]:list(i)[1]})
	return mr_dic


	
def get_allbifa():
	conn = psycopg2.connect(database='postgres',user='postgres',password='1985712',host= '54.186.47.255',options='-c statement_timeout=50000')
	cur = conn.cursor()
	cur.execute("select matches,bifa from dd_table order by matches;")
	mbifa = cur.fetchall()
	cur.close()
	conn.close()
	mb_dic = {}
	for i in mbifa:
		mb_dic.update({i[0]:list(ast.literal_eval(i[1][1:-1]))})
	return mb_dic
	


	


def bifa_rate():
	mrdic = get_allresult()
	mbdic = get_allbifa()
	merge_dic = {}
	for i in mbdic.keys():
		merge_dic.update({i:mbdic[i].append(mrdic[i])})
	return merge_dic
	