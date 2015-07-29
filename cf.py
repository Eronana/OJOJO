# -*- coding: utf-8 -*-
import urllib2
import json
import alfred
import os
def getproblem(kw):
	if kw.isdigit():
		return (int(kw),None)
	return (int(kw[:-1]),kw[-1].capitalize())
def getContestJSON(cid):
	cache='cache/CF%d.json'%cid
	if os.path.exists(cache):
		return open(cache).read().decode('gbk')
	url='http://codeforces.com/api/contest.standings?contestId=%d&from=1&count=1'%cid
	jsondata=urllib2.urlopen(url).read()
	open(cache,'w').write(jsondata)
	return jsondata
def getContest(cid):
	data=json.loads(getContestJSON(cid))
	if data["status"]!="OK":
		return None
	result={
		"id":cid,
		"name":data["result"]["contest"]["name"],
		"type":data["result"]["contest"]["type"],
		"problems":data["result"]["problems"]
	}
	return result

def add_contest(result,contest):
	url='http://codeforces.com/contest/%d'%contest["id"]
	result.append(alfred.Item(
        {
            "uid":alfred.uid(len(result)),
            "arg":url
        },
        contest["name"],
        "Type:%s Problems:%d"%(contest["type"],len(contest["problems"])),
        "13D691AA-D2EE-47FD-88FF-1653B5A6815C.png"
    ))
def add_problem(result,p):
	subtext="Index:%s"%p["index"]
	if "points" in p:
		subtext+=" Points:%d"%p["points"]
	result.append(alfred.Item(
        {
            "uid":alfred.uid(len(result)),
            "arg":'http://codeforces.com/contest/%d/problem/%s'%(p["contestId"],p["index"])
        },
        "%d%s - %s"%(p["contestId"],p["index"],p["name"]),
        subtext,
        "13D691AA-D2EE-47FD-88FF-1653B5A6815C.png"
    ))
def query(kw):
	(cid,pid)=getproblem(kw)
	contest=getContest(cid)
	if contest==None:
		return
	result=[]
	if not pid:
		add_contest(result,contest)
		for p in contest["problems"]:
			add_problem(result,p)
	else:
		for p in contest["problems"]:
			if p["index"]==pid:
			    add_problem(result,p)
			    break;
		add_contest(result,contest)
	alfred.write(alfred.xml(result))
