#coding=utf-8
import urllib.request
import time
from pyquery import PyQuery as pq
websiteurl='http://www.zfcgwssc.suzhou.gov.cn/channel/'
def gethtml(url):  
    page=urllib.request.urlopen(url)
    html=page.read().decode("utf-8")
    return html  
def geturl(ChID,PageID): #参数分类号，页码 返回url列表
    url=[]
    for i in range(1,PageID+1):
        url.append(websiteurl+str(ChID)+'_0_0_0_0_0_0_0_0.html?page='+str(i))
    return url
def getMaxPageID(ChID):
    p=pq(gethtml(websiteurl+str(ChID)))
    strPage=p('span').filter('.last')('a').attr('href')
    if strPage is None:
        return 1 
    else:
        return int(strPage.split('page=')[1].split('&')[0])
    
if __name__ == '__main__':
    start = time.clock()
    f=open('C:\\Users\\xrice\\Desktop\\py\\爬政府采购网\\dist\\商品信息'+time.strftime('%Y%m%d%H%M',time.localtime())+'.csv','w')
    for j in range(1,300): #获取1~100类商品
        urllist=geturl(j,getMaxPageID(j))
        for i in range(len(urllist)): #遍历每一页d
            d=pq(gethtml(urllist[i]))
            data1=d('div').filter('.gp-list-view') #商品信息html
            for i in data1('.info').items():
                name=i('a').eq(1).text().replace(u'\xa0', u' ').replace(u'\xb3', u' ').replace(u',', u' ')
                nameid=i('a').eq(1).attr('href').split('?p_id=')[1]
                price=i('b').attr('title').strip('¥').replace(',','')
                f.write(str(nameid)+','+str(j)+','+name+','+price+'\n') #replace(u'\xa0', u' ') 解决编码问题
        print('完成第'+str(j)+'类',round(time.clock(),2))
    f.close()    
    end = time.clock()
    print(end-start)



