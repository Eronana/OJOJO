# -*- coding: utf-8 -*-
from oj import *
class pe(oj):
	def __init__(this):
		oj.__init__(this)
		this.URL_PROBLEM='https://projecteuler.net/problem=%d'
		this.URL_PROBLEM_SET='https://projecteuler.net/archives;page=%d'
		this.DIR_CACHE='cache/PE%d.json'
		this.ICON='09F1D656-F3B0-4C0C-8808-14E775D4AEC7.png'
		this.ENCODE='utf-8'
		this.RE_QUERY=r'problem=(\d+)".*?>(.*?)<.*?>(\d+)<'
		this.CACHE_FORMAT='{"id":%s,"name":"%s","accept":%s}'
		this.BASE_PROBLEMID=1
	def pid2page(this,pid):
		return (pid-1)/50+1
	def getProblemSubtext(this,p):
		return "Accepted:%d"%(p["accept"])
	def search(this,kw):
		return