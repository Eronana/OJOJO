# -*- coding: utf-8 -*-
from oj import *
class hdu(oj):
	def __init__(this):
		oj.__init__(this)
		this.URL_PROBLEM='http://acm.hdu.edu.cn/showproblem.php?pid=%d'
		this.URL_PROBLEM_SET='http://acm.hdu.edu.cn/listproblem.php?vol=%d'
		this.URL_SEARCH='http://acm.hdu.edu.cn/search.php?action=listproblem'
		this.URL_SEARCH_PARAM='content=%s&searchmode=title'
		this.DIR_CACHE='cache/HDU%d.json'
		this.ICON='3C5AD89D-1AE3-411C-8E66-6BC0036B3EBF.png'
		this.ENCODE='gbk'
		this.RE_QUERY=r'p\(.*?\,(\d+)\,.*?,"(.*?)"\,(\d+)\,(\d+)\);'
		this.RE_SEARCH=r'showproblem\.php\?pid=(\d+)">(.*?)<.*?searchmode=source">(.*?)<.*?status=5\'>(\d+)<.*?\'>(\d+)<'
	def getSearchResult(this,p):
		name=p[1]
		source=p[2]
		(pid,ac,sub)=map(int,[p[0],p[3],p[4]])
		return {
			"url":this.URL_PROBLEM%pid,
			"title":"%d - %s"%(pid,name),
			"subtext":"Accepted:%d Submitted:%d Ratio:%.2f%% Source:%s"%(ac,sub,ac*100.0/sub,source)
		}