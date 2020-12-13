Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\Tharanithangavel\AppData\Local\Programs\Python\Python39\crd.py
>>> import crd as a
>>> a.create_key("tharani",10)
>>> a.create_key("abhi",20)
>>> a.create_key("shaar",15)
>>> a.create_key("vv",30,3200)
>>> a.create_key("blue",23,2800)
>>> a.read_key("blue")
'blue:23'
>>> a.read_key("shaar")
'shaar:15'
>>> a.read_key("abhi")
'abhi:20'
>>> a.read_key("vv")
'vv:30'
>>> a.delete_key("abhi")
key is deleted successfully
>>> a.delete_key("tharani")
key is deleted successfully
>>> a.read_key("abhi")
The given key does not exist in the data store
>>> a.read_key("shaar")
'shaar:15'
>>> a.read_key("tharani")
The given key does not exist in the data store
>>> a.read_key("blue")
'blue:23'
>>> a.create_key("swats",18,30)
>>> a.read_key("swats")
'swats:18'
>>> a.read_key("swats")
time-to-live of swats has expired
>>> 