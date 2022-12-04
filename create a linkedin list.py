# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 18:19:00 2022

@author: kn.dang
"""

class Node:
    def __init__(self, dataval):
        self.dataval = dataval 
        self.nextval = None 
        
class linkedList(): 
        
    def __init__(self,):
        
        self.firstval = None
        
e1 = Node(2)
e2 = Node(3) 
e3 = Node(5)

_list = linkedList() 
_list.firstval = Node(1)
_list.firstval.nextval = e1 

e1.nextval = e2
e2.nextval = e3

pv = _list.firstval

while pv:
    s = pv.dataval 
    pv = pv.nextval   
    print(s)
    
