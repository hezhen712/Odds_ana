import sys


class odds_trend():
	def _init_(self,home_odds,away_odds,home_name,away_name,result,match_time,match_no):
		self.home_odds = home_odds
		self.away_odds = away_odds
		self.home_name = home_name
		self.away_name = away_name
		self.match_time = match_time
		self.result = result
		self.match_no = match_no
		
	
class DD_table():
	def _init_(self,match_no,ddlist):
		self.match_no = match_no
		self.ddlist = ddlist
		
		
		
def ddlist_restruct(odds_trend):
	ddhlist = []
	ddalist = []
	for i in odds_trend.home_odds:
		new = float(i[0]) + float(i[1])
		ddhlist.append(round(new,2))
	for j in odds_trend.away_odds:
		news = float(j[0])+ float(j[1])
		ddalist.append(round(news,2))
	ddlist = ddhlist + ddalist
	return ddlist
				



	
	
