#!/usr/bin/env Python
# _*_ coding:utf-8 _*_

import string
import re
import urllib2

#create a simple spider and use it to crawl Top 100 moive's name
#from https://movie.douban.com/top250?start={page}&filter=&type=
#and output the result list

class DouBanSpider(object):
    def __init__(self):
        self.page=1
        self.current_url="http://movie.douban.com/top250?start={page}&filter=&type="
        self.data=[]
        self._top_num=1
        print " begin to scrap the top 100 movies from Douban website..."
    def get_page(self,cur_page):
        url=self.current_url
        try:
            my_page=urllib2.urlopen(url.format(page=(cur_page-1)*25)).read().decode("utf-8")
        except urllib2.URLERROR, e:
            if hasattr(e,"code"):
                print "The server could not fulfill the request."
                print "Error code is %s" %e.code
            elif hasattr(e,"reason"):
                print "We failed to reach a server。 please check your url and read the reason."
                print "Reson %s" %e.reason
        return my_page
    def find_title(self,my_page):
        temp_data=[]
        # in source html: <span class="title">肖申克的救赎</span>
        movie_items=re.findall(r'<span.*?class="title">(.*?)</span>',my_page,re.S)

    #    director_items=re.findall(r'<span.*?class="title">(.*?)</span>',my_page,re.S)
        for index,item in enumerate(movie_items):
            if item.find("&nbsp")==-1:
                temp_data.append("Top"+str(self._top_num)+" "+item)
                self._top_num+=1
        self.data.extend(temp_data)
    def start_spider(self):
        while self.page<=4:
            my_page=self.get_page(self.page)
            self.find_title(my_page)
            self.page+=1
def main():
    print "scrap Top 100 movie from moviw.douban.com"
    my_spider=DouBanSpider()
    my_spider.start_spider()
    for item in my_spider.data:
        print item
    print "finish scrap data"

if __name__=='__main__':
    main()
