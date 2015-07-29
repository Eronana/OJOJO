from oj import *
class poj(oj):
	def __init__(this):
		oj.__init__(this)
		this.URL_PROBLEM='http://poj.org/problem?id=%d'
		this.URL_PROBLEM_SET='http://poj.org/problemlist?volume=%d'
		this.URL_SEARCH='http://poj.org/searchproblem'
		this.URL_SEARCH_PARAM='key=%s&field=title&B1=GO'
		this.DIR_CACHE='cache/POJ%d.json'
		this.ICON='3D2A4631-525A-4CE4-88F6-66AEFB4DE0E1.png'
		this.ENCODE='utf-8'
		this.RE_QUERY=r'problem\?id=(\d+)>(.*?)<.*?problem_id=\d+>(\d+)<.*?problem_id=\d+>(\d+)<'
		this.RE_SEARCH=r'problem\?id=(\d+)>(.*?)<.*?target=_blank>(\d+)</a></td><td>(.*?)</td>'
	def getSearchResult(this,p):
		name=p[1]
		source=p[3]
		(pid,ac)=map(int,[p[0],p[2]])
		return {
			"url":this.URL_PROBLEM%pid,
			"title":"%d - %s"%(pid,name),
			"subtext":"Solved:%d Source:%s"%(ac,source)
		}