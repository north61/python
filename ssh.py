#!/usr/bin/env python  
import paramiko  

ipaddrs = {}  

def main():  
    pass

def exec_command(ip,username,password,port,command):
    client = paramiko.SSHClient()  
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
    client.connect(hostname=ip,port=port,username=username,password=password)  
    stdin, stdout, stderr = client.exec_command(command)  
    #print 'stderr', stderr  
    #print 'stdout', type(stdout)  
    for line in stdout:  
        print '...' + line.strip('\n')  
    client.close()  
    print 'close'  

def upload_file(ip,username,password,port,localfile,remotefile):
    t = paramiko.Transport((ip,port))
    t.connect(username = username, password = password)
    sftp = paramiko.SFTPClient.from_transport(t)
    remotepath= remotefile
    localpath= localfile
    sftp.put(localpath,remotepath)
    t.close()


def download_file(ip,username,password,port,localfile,remotefile):
    t = paramiko.Transport((ip,port))
    t.connect(username = username,password = password )
    sftp = paramiko.SFTPClient.from_transport(t)
    remotepath= remotefile
    localpath= localfile
    sftp.get(remotepath, localpath)
    t.close()

if __name__ == '__main__':  
    main()  
