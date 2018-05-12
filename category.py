#coding=utf-8
import time
import urllib.request
from pyquery import PyQuery as pq
def gethtml(url):  
    page=urllib.request.urlopen(url)
    html=page.read().decode("utf-8")
    #html=page.read().decode("utf-8")
    return html  
if __name__=='__main__':
    p=pq(gethtml('http://www.zfcgwssc.suzhou.gov.cn/'))
    for i in p('span').items():
        j=i('a').attr('href').split('channle/')
        if  j!= None:
            print(j)             
        
    print('ok')