class Tree(object):
	def __init__(self, label, left, right):
		self.left = left
		self.right = right
		self.label = label
        
def es_literal(f):
	# Esta función determina si el árbol f es un literal
	# Input: f, una fórmula como árbol
    if f.left == None:
        if f.right == None or f.right.right == None:
            return True
        else:
            return False
    else:
    	return False
    # Output: True/False

f = Tree('-',None,Tree('p',None,None))
f1 = Tree('O',Tree('k',None,None),Tree('Y',Tree('i',None,None),Tree('j',None,None)))
f2 = Tree('alpha',None,None)
f3 = Tree('-',None,Tree('Y',Tree('p',None,None),Tree('q',None,None)))
#print(es_literal(f3))

def no_literales(l):
	# Esta función determina si una lista de fórmulas contiene
	# solo literales
	# Input: l, una lista de fórmulas como árboles
	# Output: None/f, tal que f no es literal
    for f in l:
        if es_literal(f) == False:
            return False
        m = True
    return m

f3 = [Tree('q',None,None),Tree('-',None,Tree('p',None,None)),Tree('-',None,Tree('-',None,Tree('p',None,None))),Tree('-',None,Tree('q',None,None))]
f4 = [Tree('-',None,Tree('A1',None,None)),Tree('A2',None,None),Tree('-',None,Tree('A3',None,None)),Tree('A4',None,None),Tree('-',None,Tree('A5',None,None)),Tree('A6',None,None)]
f5 = [Tree('p',None,None),Tree('q',None,None),Tree('O',Tree('p',None,None),Tree('q',None,None)),Tree('-',None,Tree('q',None,None)),Tree('-',None,Tree('p',None,None))]
f6 = [Tree('-',None,Tree('p',None,None)),Tree('p',None,None),Tree('-',None,Tree('q',None,None)),Tree('q',None,None)]

print(no_literales(f6))