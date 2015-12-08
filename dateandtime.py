#-*- coding: UTF-8 -*-
# coding=gbk
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import json
import urllib2
from bs4 import BeautifulSoup
import time
import pymongo

def date2id (year,date):
    if date.startswith('Jan'):
        return year+'01'+date[4:].zfill(2)
    elif date.startswith('Feb'):
        return year+'02'+date[4:].zfill(2)
    elif date.startswith('Mar'):
        return year+'03'+date[4:].zfill(2)
    elif date.startswith('Apr'):
        return year+'04'+date[4:].zfill(2)
    elif date.startswith('May'):
        return year+'05'+date[4:].zfill(2)
    elif date.startswith('Jun'):
        return year+'06'+date[4:].zfill(2)
    elif date.startswith('Jul'):
        return year+'07'+date[4:].zfill(2)
    elif date.startswith('Aug'):
        return year+'08'+date[4:].zfill(2)
    elif date.startswith('Sep'):
        return year+'09'+date[4:].zfill(2)
    elif date.startswith('Oct'):
        return year+'10'+date[4:].zfill(2)
    elif date.startswith('Nov'):
        return year+'11'+date[4:].zfill(2)
    elif date.startswith('Dec'):
        return year+'12'+date[4:].zfill(2)


url='http://www.timeanddate.com/holidays/sweden/2015'
req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
cont = urllib2.urlopen(req).read()
soup = BeautifulSoup(cont, "lxml")

for tr in soup.find('tbody').findAll('tr'):
    date = tr.th.text
    id=date2id('2015',date)
    # print date,
    print id,
    print tr.td.nextSibling.text
    url = 'http://www.timeanddate.com'+tr.td.nextSibling.a['href']
    req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
    cont = urllib2.urlopen(req).read()
    soup1 = BeautifulSoup(cont, "lxml")
    try:
        print soup1.find('p',{'class':'lead'}).text
    except:
        pass
    # break
























