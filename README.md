# wooyun-bug_crawler
# 功能描述：
该程序分为两部分，准确地说是两个程序，分别运行来达到爬取乌云上的bugs的目的


1.第一部分（scraptor）
  根据页码扫描网站获取漏洞的Url，并将Urls储存再txt文档中
  
2.第二部分（collector）
  程序读取上一步产生的txt文档，依次爬取所需信息，写入一个新的txt文档中，格式依照csv，可以方便地导入excel或者数据库
