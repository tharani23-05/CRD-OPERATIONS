import threading 
from threading import*
import time

d={} 

def create_key(key,value,timeout=0):
    if key in d:
        print("this key already exists") 
    else:
        if(key.isalpha()):
            if len(d)<(1024*1020*1024) and value<=(16*1024*1024): 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: 
                    d[key]=l
            else:
                print("Memory limit exceeded!")
        else:
            print("Invalind key name!")

def delete_key(key):
    if key in d:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                del d[key]
                print("key is deleted successfully")
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            del d[key]
            print("key is deleted successfully")
        
    else:
        print("The given key does not exist in the data store") 
            
def read_key(key):
    if key in d:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                string=str(key)+":"+str(b[0]) 
                return string
            else:
                print("time-to-live of",key,"has expired") 
        else:
            string=str(key)+":"+str(b[0])
            return string
    else:
        print("The given key does not exist in the data store") 
        


        

