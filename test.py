#coding=utf-8
import time
import urllib.request
from pyquery import PyQuery as pq
def getHtml(url):
    req = urllib.request.Request(url, headers = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
        })
    oper = urllib.request.urlopen(req)
    data = oper.read().decode("utf-8")
    return data
if __name__=='__main__':
    url='http://www.zhainanmao.com/4994.html'
    print(getHtml(url))
    p=pq(getHtml(url))
    for i in p('div').filter('single-text').items():
        print(i)
    