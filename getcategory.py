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
    starttime=time.clock()
    f=open('categorylist.csv','w')
    for i in p('span').items():
        j=i('a').attr('href')
        if j is None:
            pass
        else:
            k=j.split('nel/')
            if len(k)==2:
                f.write(i('a').text()+','+k[1]+'\n')
    f.close()
    print(time.clock()-starttime)               
    print('ok')