# -*- coding:utf-8 -*-
import urllib
import urllib2
import re 
 
url = 'https://www.aqistudy.cn/historydata/daydata.php?city=%E5%AE%89%E9%98%B3&month=2014-01'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<tr>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>(.*?)(.*?)(.*?)(.*?)</tr>',re.S)
    items = re.findall(pattern,content)
    for item in items:
        print item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8],item[9]
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
