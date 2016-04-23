# -*- coding: utf-8 -*-
#this is a program to collect all the bugs imformations
#and store them in a Excel sheet
#the program read the bugs url from the txt file

import urllib2
from BeautifulSoup import *
import sys
import re
import threading

errors = 0
Urls =[]
counter = 0

threadlock = threading.Lock()
class Multhread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name
    
    def run(self):
        print 'starting ',self.name
        OpenUrls(Urls,self)
        
def parse_write(tags):
    '''
    this function is use for parsing the website and write into the txt file.
    the format o fthe data is csv
    '''
    bug_infor = {}
    bug_infor['title'] = re.findall('漏洞标题：		(.*?)<',tags)[0]
    bug_infor['company'] = re.findall(u'www.wooyun.org/corps/(.*?)"',tags)[0]
    bug_infor['author'] = re.findall(u'www.wooyun.org/whitehats/(.*?)"',tags)[0]
    bug_infor['handin_time'] = re.findall('提交时间：		(.*?)</h3>',tags)[0]
    bug_infor['publish_time'] = re.findall('公开时间：		(.*?)</h3>',tags)[0]
    bug_infor['bug_type'] = re.findall('漏洞类型：		(.*?)</h3>',tags)[0]
    bug_infor['self_rank'] = re.findall('自评Rank：		(.*?)</h3>',tags)[0]
    bug_infor['harm_rank'] = re.findall('危害等级：		(.*?)</h3>',tags)[0]


#因为excel这个不好用，所以先尝试写入txt

    f = open('collection.txt','a')
    infor = '''"'''+bug_infor['title']+'''"''' + ',' +\
        '''"'''+bug_infor['company']+'''"''' + ',' +\
        '''"'''+bug_infor['author']+'''"''' + ',' +\
        '''"'''+bug_infor['handin_time']+'''"''' + ',' +\
        '''"'''+bug_infor['publish_time']+'''"''' + ',' +\
        '''"'''+bug_infor['bug_type']+'''"''' + ',' +\
        '''"'''+bug_infor['self_rank']+'''"''' + ',' +\
        '''"'''+bug_infor['harm_rank']+'''"'''
        
    f.write( infor + '\n')


    
def OpenUrls(Urls,self):
    '''
    this funtion is used to open the webpage and get the data then call parse_write 
    '''  
    global counter
    global errors
    while counter < 38099:
        threadlock.acquire()
        url = Urls[counter]
        try:
            html = urllib2.urlopen(url,timeout = 10).read()
            soup = BeautifulSoup(html)
            tags = str(soup('h3'))
        except:
            errors += 0     
        try:
            parse_write(tags)
            print self.name,'is working on ',counter
        except:
            errors += 0
        counter += 1
        threadlock.release()
            
            
def file2list(Urls):
    '''
    take no arguement convert the txt to list,each line is an element
    '''
    try:
        handle = open('/Users/leomarch/Desktop/bugs.txt')  #open the file of urls
    except:
        print 'file not found'
        sys.exit()
    for line in handle:
        Urls.append(str(line)[:-1])
        
        
        
file2list(Urls)
threads = []
thread1 = Multhread('name1')
thread2 = Multhread('name2')
thread3 = Multhread('name3')
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)

thread1.start()
thread2.start()
thread3.start()

# for t in threads:
#      t.join()