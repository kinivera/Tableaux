def complementol(l):
    if len(l) %2 == 0 :
        return l[len(l)-1]
    else :
        return "-"+l

def complemento(l):
    if l.label =="-":
        return l.right.label
    else :
        return "-"+l.label
 

#print(complemento(l))

def par_complementariol(h):
    for i in range (len(h)):
       for j in range (i+1,len(h)): 
           if h[i]== complementol(h[j]):
               print(h[i])
               return True
               break
    return False

def par_complementario(h):
    for i in range (len(h)):
       for j in range (i+1,len(h)): 
           p=h[i]
           l=h[j] 
           if p.label == complemento(l.label):
               print(h[i])
               return True
               break
    return False

a=[Tree('b',None,None), Tree('-',None,Tree('a',None,None)), Tree('-',None,Tree('c',None,None)), Tree('a',None,None), Tree('d',None,None)]
b=["b","-a","-c","a","d"]
c=["p", "q", "-p","r","q"]

print(par_complementario(a))