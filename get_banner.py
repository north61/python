import requests
import Queue
import threading,os
from bs4 import BeautifulSoup


url_q = Queue.Queue()
result_q = Queue.Queue()

def insert_urlQueue():
    with open('url.txt','r') as f:
        for line in f:
            url_q.put(line)
 
        
class get_titleThread(threading.Thread):
    def __init__(self,thread_id,q):
        threading.Thread.__init__(self)
	self.thread_id = thread_id
        self.q = q    

    def run(self):
        print "Starting " + self.name
        request_http(self.q,self.thread_id)
        print "Exiting " + self.name 
    
def request_http(q,thread_id):
    while q.empty() != True:
        domain = q.get()          
        r1 = requests.get("https://"+domain.rstrip(),verify=False)
        result_q.put(r1)
        r2 = requests.get("http://"+domain.rstrip(),verify=False)
        result_q.put(r2)

def insert_result(q):

        while not q.empty():
	    r = q.get()

            print r.url,r.status
            f.write(r.url + "," + r.status_code+ "," + title)
        

def main():
    insert_urlQueue()
    threads = []
    for i in range(10):
    	t = get_titleThread(i,url_q)
    	t.start()
        threads.append(t)
    for t in threads:
        t.join()
    #insert_result(result_q)
    with open('banner.txt','w') as f:
        while not result_q.empty():
            r = result_q.get()
            soup = BeautifulSoup(r.content, "lxml")
            res1 = "{}".format(r.url)+ ",{}".format(str(r.status_code))+"," + "{}".format(str(soup.title).strip())+os.linesep
            print  res1
            f.write(res1)
    

if __name__ == "__main__":
    main()


