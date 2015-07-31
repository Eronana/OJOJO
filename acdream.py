# -*- coding: utf-8 -*-
from oj import *
class ac(oj):
	def __init__(this):
		oj.__init__(this)
		this.URL_PROBLEM='http://acdream.info/problem?pid=%d'
		this.URL_PROBLEM_SET='http://acdream.info/problem/list?page=%d'
		this.URL_SEARCH='http://acdream.info/problem/list?search=%s'
		this.DIR_CACHE='cache/AC%d.json'
		this.ICON='01D15B7B-DDA4-4886-A0E9-EFED15EA6AF0.png'
		this.ENCODE='utf-8'
		this.RE_SEARCH=this.RE_QUERY=r'problem\?pid=(\d+)">(.*?)<.*?tag">(.*?)<.*?result=2">(\d+)<.*?">(\d+)<'
		this.CACHE_FORMAT='{"id":%s,"name":"%s","source":"%s","accept":%s,"submut":%s}'
	def pid2page(this,pid):
		pageindex=[0,1058,1111,1161,1214,1414,1762]
		for i in range(len(pageindex)):
			if pid<=pageindex[i]:
				return i
		return (pid-1000)/127+1
	def getProblemSubtext(this,p):
		return "%s Source:%s"%(oj.getProblemSubtext(this,p),p["source"])
	def getSearchHTML(this,kw):
		return this.geturl(this.URL_SEARCH%kw).decode(this.ENCODE)
	def getSearchResult(this,p):
		return oj.getQueryResult(this,json.loads(this.CACHE_FORMAT%tuple(p)))