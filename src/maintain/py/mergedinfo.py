#!/usr/bin/env python
# -*- coding:utf-8 -*-

from cpuinfo import *
from diskinfo import *
from hostinfo import *
from ipaddress import *
from meminfo import *
from product import *
import urllib
import urllib2

def getHostTotal():
    ld = []
    cpuinfo = parserCpuInfo(getCpuInfo())
    diskinfo = parserDiskInfo(getDiskInfo())
    for i in  parserMemInfo(getMemInfo()):
        meminfo = i
    productinfo = parserDMI(getDMI())
    hostinfo = getHostInfo()
    ipaddr = parserIpaddr(getIpaddr())
    for i in ipaddr:
        ip = i
    for k in cpuinfo.iteritems():
        ld.append(k)
    for i in diskinfo.iteritems():
        ld.append(i)
    for j in meminfo.iteritems():
        ld.append(j)
    for v in productinfo.iteritems():
        ld.append(v)
    for x in hostinfo.iteritems():
        ld.append(x)
    for y in ip.iteritems():
        ld.append(y)
    return ld

def parserHostTotal(hostdata):
    pg = {}
    for i in hostdata:
        pg[i[0]] = i[1]
    return pg

def urlPost(postdata):
    data = urllib.urlencode(postdata)
    req = urllib2.Request('http://127.0.0.1:8000/api/collect', data)
    response = urllib2.urlopen(req)
    return response.read()

if __name__ == '__main__':
    hostdata = getHostTotal()
    postdata = parserHostTotal(hostdata)
    print urlPost(postdata)

