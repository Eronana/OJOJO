# -*- coding: utf-8 -*-
from oj import *
class sgu(oj):
	def __init__(this):
		oj.__init__(this)
		this.URL_PROBLEM='http://acm.sgu.ru/problem.php?contest=0&problem=%d'
		this.URL_PROBLEM_SET='http://acm.sgu.ru/problemset.php?contest=0&volume=%d'
		this.DIR_CACHE='cache/SGU%d.json'
		this.ICON='09F1D656-F3B0-4C0C-8808-14E775D4AEC7.png'
		this.ENCODE='cp1251'
		this.RE_QUERY=r'>(\d+)</a></td><td>&nbsp;(.*?)<.*?contest=0>(\d+)<'
		this.CACHE_FORMAT='{"id":%s,"name":"%s","accept":%s}'
		this.BASE_PROBLEMID=100
	def pid2page(this,pid):
		return pid/100
	def getProblemSubtext(this,p):
		return "Accepted:%d"%(p["accept"])
	def search(this,kw):
		return