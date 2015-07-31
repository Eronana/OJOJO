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
		this.BASE_PROBLEMID=1000
		this.BEGIN_PROBLEMID=0
		this.BASE_PAGE=1
		this.PRE_PAGE=1
		this.FAILCOUNT=5
	def geturl(this,url,data=''):
		open("url.txt","a").write(url+'\n')
		if data=='':
			data=None
		req=urllib2.Request(url)
		req.add_header('User-Agent',this.USER_AGENT)
		return urllib2.urlopen(req,data).read()
	def pid2page(this,pid):
		return (pid-1000)/100+1
	def getProblemID(this,p):
		return int(p[0])
	def getProblemURL(this,p):
		return this.URL_PROBLEM%p["id"]
	def getProblemTitle(this,p):
		return "%d - %s"%(p["id"],p["name"])
	def getProblemSubtext(this,p):
		return "Accepted:%d Submitted:%d Ratio:%.2f%%"%(p["accept"],p["submut"],p["accept"]*100.0/p["submut"])
	def getQueryResult(this,p):
		return {
			"url":this.getProblemURL(p),
			"title":this.getProblemTitle(p),
			"subtext":this.getProblemSubtext(p)
		}
	def getProblemJSON(this,pid,get=True):
		cache=this.DIR_CACHE%pid
		if os.path.exists(cache):
			return open(cache).read().decode(this.ENCODE)
		if not get:
			return None
		page=this.pid2page(pid)
		minprob=2100000000
		cnt=0
		while page>=this.BASE_PAGE and minprob>pid:
			cnt+=1
			if cnt>this.FAILCOUNT:
				break
			url=this.URL_PROBLEM_SET%page
			html=this.geturl(url)
			problems=re.compile(this.RE_QUERY,re.DOTALL).findall(html)
			page-=this.PRE_PAGE
			if problems==[]:
				break
			minprob=this.getProblemID(problems[0])
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
	def getproblem(this,pid,isget=True):
		data=this.getProblemJSON(pid,isget)
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

	def add_problem(this,result,pid,isget=True):
		if pid <this.BASE_PROBLEMID+this.BEGIN_PROBLEMID:
			return True
		p=this.getproblem(pid,isget)
		if p==None:
			return False
		this.ad_prob(result,this.getQueryResult(p))
		return True
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
	def getProblemList(this,pid):
		result=[]
		if pid<this.BASE_PROBLEMID:
			while pid<this.BASE_PROBLEMID/10:
				pid*=10
			for i in range(10):
				result.append(pid*10+i)
		else:
			result.append(pid)
		return result
	def query(this,pid):
		if pid==0:
			return
		result=[]
		isget=True
		for p in this.getProblemList(pid):
			isget=this.add_problem(result,p,isget)
		this.checkresult(result,"No this problem %d"%pid)
		alfred.write(alfred.xml(result))
	def getSearchHTML(this,kw):
		return this.geturl(this.URL_SEARCH,this.URL_SEARCH_PARAM%kw).decode(this.ENCODE)
	def search(this,kw):
		html=this.getSearchHTML(kw)
		problems=re.compile(this.RE_SEARCH,re.DOTALL).findall(html)
		result=[]
		for p in problems:
			this.ad_prob(result,this.getSearchResult(p))
		this.checkresult(result,"No result found")
		alfred.write(alfred.xml(result))