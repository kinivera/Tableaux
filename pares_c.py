# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 15:40:07 2020

@author: 57313
"""

#lista normal 
def complementol(l):
    if len(l) %2 == 0 :
        return l[len(l)-1]
    else :
        return "-"+l
#en forma de arbol 
def complemento(l):
    if l.label =="-":
        return l.right.label
    else :
        return "-"+l.label
 

#print(complemento(l))

#cuando esta como lista de literales 
def par_complementariol(h):
    for i in range (len(h)):
       for j in range (i+1,len(h)): 
           if h[i]== complemento(h[j]):
               print(h[i])
               return True
               break
       return False
   
#cuando la lista de literales estan en arbol 
def par_complementario(h):
    for i in range (len(h)):
       for j in range (i+1,len(h)): 
           if h[i]== complemento(h[j]):
               print(h[i])
               return True
               break
       return False

h=[Tree('-',None,Tree('Z1',None,None)), Tree('S1',None,None), Tree('-',None,Tree('S10',None,None)), Tree('Z10',None,None)]
print(par_complementario(h))
