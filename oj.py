# -*- coding: utf-8 -*-
import urllib2
import urllib
import json
import alfred
import os
import re
class oj:
	def __init__(this):
		this.USER_AGENT='Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
		this.CACHE_FORMAT='{"id":%s,"name":"%s","accept":%s,"submut":%s}'
	def geturl(this,url,data=''):
		if data=='':
			data=None
		req=urllib2.Request(url)
		req.add_header('User-Agent',this.USER_AGENT)
		return urllib2.urlopen(req,data).read()
	def pid2page(this,pid):
		return (pid-1000)/100+1
	def getProblemID(this,p):
		return int(p[0])
	def getQueryResult(this,p):
		return {
			"url":this.URL_PROBLEM%p["id"],
			"title":"%d - %s"%(p["id"],p["name"]),
			"subtext":"Accepted:%d Submitted:%d Ratio:%.2f%%"%(p["accept"],p["submut"],p["accept"]*100.0/p["submut"])
		}
	def getProblemJSON(this,pid,get=True):
		cache=this.DIR_CACHE%pid
		if os.path.exists(cache):
			return open(cache).read().decode(this.ENCODE)
		if not get:
			return None
		page=this.pid2page(pid)
		url=this.URL_PROBLEM_SET%page
		html=this.geturl(url)
		problems=re.compile(this.RE_QUERY,re.DOTALL).findall(html)
		for x in problems:
			p=[]
			for i in x:
				p.append(i.replace('"','\\"'))
			p=tuple(p)
			jsonstr=this.CACHE_FORMAT%p
			jsonfile=this.DIR_CACHE%this.getProblemID(p)
			if not os.path.exists(jsonfile):
				open(jsonfile,'w').write(jsonstr)
		return this.getProblemJSON(pid,False)
	def getproblem(this,pid):
		data=this.getProblemJSON(pid)
		return json.loads(data) if data!=None else None
	def ad_prob(this,result,p):
		result.append(alfred.Item(
	        {
	            "uid":alfred.uid(len(result)),
	            "arg":p["url"]
	        },
	        p["title"],
	        p["subtext"],
	        this.ICON
	    ))

	def add_problem(this,result,pid):
		p=this.getproblem(pid)
		if p==None:
			return
		this.ad_prob(result,this.getQueryResult(p))
	def checkresult(this,result,hit):
		if len(result)==0:
			result.append(alfred.Item(
				{
					"uid":alfred.uid(len(result))
				},
				hit,
				None,
				this.ICON
			))
	def query(this,pid):
		if pid==0:
			return
		result=[]
		if pid<1000:
			xpid=pid
			while xpid<100:
				xpid*=10
			for i in range(10):
				this.add_problem(result,xpid*10+i)
		else:
			this.add_problem(result,pid)
		this.checkresult(result,"No this problem %d"%pid)
		alfred.write(alfred.xml(result))
	def getSearchHTML(this,kw):
		return this.geturl(this.URL_SEARCH,this.URL_SEARCH_PARAM%kw).decode(this.ENCODE)
	def search(this,kw):
		html=this.getSearchHTML(kw)
		problems=re.compile(this.RE_SEARCH,re.DOTALL).findall(html)
		result=[]
		for p in problems[:10]:
			this.ad_prob(result,this.getSearchResult(p))
		this.checkresult(result,"No result found")
		alfred.write(alfred.xml(result))