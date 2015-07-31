# -*- coding: utf-8 -*-
from oj import *
class spoj(oj):
	def __init__(this):
		oj.__init__(this)
		this.DIR_CACHE='cache/SPOJ%d.json'
		this.URL_PROBLEM='http://www.spoj.com/problems/%s/'
		this.ICON='8E3ED658-BB90-4830-AAB2-DE051F29BB11.png'
		this.ENCODE='utf-8'
		this.RE_QUERY=r'<td class="text-center">\s+(\d+).*?href="/problems/(.*?)/">(.*?)<.*?title=".*?>(\d+)<.*?>([\.\-\d+]+)<'
		this.CACHE_FORMAT='{"id":%s,"urlname":"%s","name":"%s","users":%s,"acc":%s}'
		this.BASE_PROBLEMID=1
		this.BASE_PAGE=0
		this.PRE_PAGE=50
	def pid2page(this,pid):
		for i in range(len(this.pageindex)):
			if pid<=this.pageindex[i]:
				return i*50
		return pid-this.pageindex[-1]
	def getProblemURL(this,p):
		return this.URL_PROBLEM%p["urlname"]
	def getProblemSubtext(this,p):
		return "USERS:%d ACC:%.2f%%"%(p["users"],p["acc"])
	def getClassicalJSON(this,pid,get=True):
		this.pageindex=[54,112,203,296,388,677,904,1420,1553,1744,1874,2136,2325,2737,3033,3382,3591,3890,3982,4194,4455,4784,5160,5832,6377,6819,7107,7356,7629,7861,8106,8407,8626,8916,9185,9527,9788,10070,10264,10463,10621,10966,11443,11772,12076,12436,12978,13384,13826,14697,14956,15310,15609,16063,16482,17559,18186,18799,19308,20673,21178,22037,22784,24258,24874]
		this.URL_PROBLEM_SET='http://www.spoj.com/problems/challenge/sort=0,start=%d'
		return oj.getProblemJSON(this,pid,get)
	def getChallengeJSON(this,pid,get=True):
		this.pageindex=[2624,12393,22739]
		this.URL_PROBLEM_SET='http://www.spoj.com/problems/challenge/sort=0,start=%d'
		return oj.getProblemJSON(this,pid,get)
	def getPartialJSON(this,pid,get=True):
		this.pageindex=[3807,12947,17310,22466]
		this.URL_PROBLEM_SET='http://www.spoj.com/problems/partial/sort=0,start=%d'
		return oj.getProblemJSON(this,pid,get)
	def getTutorialJSON(this,pid,get=True):
		this.pageindex=[2156,4138,5848,7675,8440,9173,10365,11317,11995,12523,13401,14120,14868,15635,16118,18039,19289,20748,21647,22340,23432,24737]
		this.URL_PROBLEM_SET='http://www.spoj.com/problems/tutorial/sort=0,start=%d'
		return oj.getProblemJSON(this,pid,get)
	def getRiddleJSON(this,pid,get=True):
		this.pageindex=[22767]
		this.URL_PROBLEM_SET='http://www.spoj.com/problems/riddle/sort=0,start=%d'
		return oj.getProblemJSON(this,pid,get)
	def getProblemJSON(this,pid,get=True):
		data=this.getClassicalJSON(pid,get)
		if data==None:
			data=this.getChallengeJSON(pid,get)
		if data==None:
			data=this.getPartialJSON(pid,get)
		if data==None:
			data=this.getTutorialJSON(pid,get)
		if data==None:
			data=this.getRiddleJSON(pid,get)
		return data
