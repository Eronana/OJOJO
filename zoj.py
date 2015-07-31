# -*- coding: utf-8 -*-
from oj import *
class zoj(oj):
	def __init__(this):
		oj.__init__(this)
		this.URL_PROBLEM='http://acm.zju.edu.cn/onlinejudge/showProblem.do?problemCode=%d'
		this.URL_PROBLEM_SET='http://acm.zju.edu.cn/onlinejudge/showProblems.do?contestId=1&pageNumber=%d'
		this.URL_SEARCH='http://acm.zju.edu.cn/onlinejudge/searchProblem.do?contestId=1&titlefrom=0&authorfrom=0&sourcefrom=0&query=%s'
		this.DIR_CACHE='cache/ZOJ%d.json'
		this.ICON='AC929DE7-F240-4ADE-A7F2-DDFBE4943538.png'
		this.ENCODE='gbk'
		this.RE_QUERY=r'problemTitle.*?problemCode=(\d+)">.*?>(.*?)<.*?judgeReplyIds=5\'>(\d+)<.*?=\d+\'>(\d+)<'
		this.RE_SEARCH=r'problemTitle.*?problemCode=(\d+)">.*?>(.*?)<'
		this.BEGIN_PROBLEMID=1
	def pid2page(this,pid):
		if pid>3001:
			pid-=2
		elif pid>2900:
			pid-=1
		return (pid-(1000)-1)/100+1
	def getSearchHTML(this,kw):
		return this.geturl(this.URL_SEARCH%kw).decode(this.ENCODE)
	def getSearchResult(this,p):
		pid=int(p[0])
		name=p[1]
		return {
			"url":this.URL_PROBLEM%pid,
			"title":"%d - %s"%(pid,name),
			"subtext":None
		}