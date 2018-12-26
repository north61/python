#!/usr/bin/env python
# -*- conding:utf-8 -*- 
import urllib.request
import urllib.error
import threading
import queue
import time
 
q=queue.Queue()
list = []
name = input("文件名：")
with open('%s'%(name), 'r') as f:
    for i in f.readlines():
        i = i.strip()
        q.put(i)
 
print(q.qsize())  #显示一共多少个链接
 
class mythread(threading.Thread):
    def __init__(self,q):
        threading.Thread.__init__(self)
        self.q = q
 
    def run(self):
        while self.q.empty() == False:  #判断q是否还有链接
            url = self.q.get()
            urls = "http://"+url
            try:
                opurl = urllib.request.urlopen(urls, timeout=3).code
                print(url + " --------->" + str(opurl))
                list.append(urls)
            except urllib.error.URLError as e:
                print(e)
                e = str(e)
                if 'SSL' in e:
                    list.append("https://" + url)
                    print("https://" + url + " ---> https")
                print(urls + ' --->错误')
            except:
                print(urls + " -------->错误！！")
 
threads = []
for i in range(10):  #多线程启动
    thread1 = mythread(q)
    thread1.start()
    threads.append(thread1)
 
# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")
 
with open('%s_200.txt'%(name),'a') as f:
    for i in list:
        f.write(i+'\n')
