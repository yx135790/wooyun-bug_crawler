# -*- coding: utf-8 -*-
import urllib2
from BeautifulSoup import *
import re
import threading
    
def collector(p):    
    url_raw = 'http://www.wooyun.org/bugs/new_public/page/'

    # the range function is used to keep the program from running forever
    
    url = url_raw +str(p)
    #renew the page url by replace the page number
    
    request_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept':'text/html;q=0.9,*/*;q=0.8',
    'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Connection':'close',
    'Referer':None 
    }
    request = urllib2.Request(url,None,request_headers)
    html = urllib2.urlopen(request,timeout=10).read()
    html = html.decode('utf8')
    soup = BeautifulSoup(html)
    tags = soup('a')

    #this is a section to wait for the website because the web has defense 
    while True:
        if '如果长时间没有跳转，请点击这里'in str(tags):
            print 'waiting for the website'
            html = urllib2.urlopen(url).read()
            soup = BeautifulSoup(html)
            tags = soup('a')
        else:    
            print 'no error'
            break
            
            
    #Retrieve a list of the anchor tags
    for tag in tags:
        urls = re.findall('^<a href="(/bugs/wooyun.*)"',str(tag))
        if urls != []:
            urls = 'http://www.wooyun.org' + str(urls[0])
            f = open('bugs.txt','a')
            f.write(urls + '\n')
            #get the url of the bugs and write it in the file
    url = url_raw + str(p + 1)
    #renew the page url by replace the page numbe


threadLock = threading.Lock()
threads = range(100)
page = 0
class MultiThreads(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        threadLock.acquire()
        global page
        while page <= 1904:
            try:
                collector(page)
                print 'working on the page' ,page
                page += 1
            except:
                break
        threadLock.release()

        
for t in threads:
    threads[t] = "thread" + str(t)
    threads[t] = MultiThreads("name")
    threads[t].start()      

for t in threads:
    t.join()
    
print 'Done'