import crawl_engine
import sys,database_conn,data_class_test
import sys,os,re
import urllib2,psycopg2
from pearson_correlations import get_mdic,get_list,lst_cmp

def winrate():
	mdic = get_mdic()
	mr = get_allresult()
	winrate = {}
	act_res = {}
	for i in mdic.keys():
		res = comp_all(i)
		winrate.update({mr[i]:res})
	return winrate

		
def comp_all(mn):	
	mdic = get_mdic()
	list1 = mdic[str(mn)]
	com_res = {}
	res = {}
	for i in mdic.keys():
		if abs(len(mdic[i])-len(list1))<= 5 and i !=str(mn):
			com_res.update({i:lst_cmp(list1,mdic[i])})
	for j in com_res.keys():
		if com_res[j] >0.5:
			res.update({j:com_res[j]})
	return res
	
def get_allresult():
	conn = psycopg2.connect(database='postgres',user='postgres',password='1985712',host= '54.186.47.255',options='-c statement_timeout=10000')
	cur = conn.cursor()
	cur.execute("select mnumber,result from _odds_trend order by mnumber;")
	mres = cur.fetchall()
	cur.close()
	conn.close()
	mr_dic = {}
	for i in mres:
		mr_dic.update({list(i)[0]:list(i)[1]})
	return mr_dic