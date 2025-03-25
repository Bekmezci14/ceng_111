
def notnested(T):
    # listeyi düzlüyor  --çalışıyor
    if len(T)==0:
        return []
    for y in T:
        if type(y)==str:
            return [y] + notnested(T[1:])
        if type(y)==list:
            return notnested(y) + notnested(T[1:])

def find(T, x):
    # bulunduğu listeyi veriyor  --çalışıyor
    for y in T:
        if y==x: return T
        if type(y)==list:
            if find(y, x)==None:
                continue
            return find(y, x)


def root(T, x):
    # atasını veriyor --çalışıyor
    if T[0]==x:
        return ["x"]
    a = find(T, x)[0]
    if a!=x:
        return a
    else:
        return find(T, find(T, x))[0]


def katman(T, x):
    # kaçıncı nested listede   
    for y in T:
        if x ==y:
            return 1 
    for y in T:
        if type(y)==list:
            if katman(y,x)!=None:
                return katman(y, x) + 1
            
            
def nesil(T, x):
    # tree deki katmanı  --çalışıyor
    if find(T,x)[0]==x:
        return katman(T,x) - 1
    return katman(T, x)

def male(x):
    return x[0]==x.lower()[0]
   

def siblings(T, x):    #çalışıyor   
    tree = notnested(T) 
    nesilx = nesil(T,x)
    rootx = root(T, x)
    listem = []
    for y in tree:
        if nesil(T, y)==nesilx:
            if root(T, y)==rootx:
                listem.append(y)
    if x in listem:
        listem.remove(x)
    return listem

def brothers(T, x):     #çalışıyor
    tree = notnested(T) 
    nesilx = nesil(T,x)
    rootx = root(T, x)
    listem = []
    for y in tree:
        if nesil(T, y)==nesilx:
            if root(T, y)==rootx:
                if male(y):
                    listem.append(y)
    if x in listem:
        listem.remove(x)
    return listem

def sisters(T, x):
    tree = notnested(T) 
    nesilx = nesil(T,x)
    rootx = root(T, x)
    listem = []
    for y in tree:
        if nesil(T, y)==nesilx:
            if root(T, y)==rootx:
                if not male(y):
                    listem.append(y)
    if x in listem:
        listem.remove(x)
    return listem

def cousins(T, x):
    tree = notnested(T) 
    nesilx = nesil(T,x)
    rootx = root(T, x)
    if nesilx<2:
        return []
    listem =[]
    grandx = root(T, rootx)
    for y in tree:
        if nesil(T,y)<2: continue
        if nesil(T,y)==nesilx:
            if root(T, root(T,y))==grandx:
                if root(T, y)!=rootx:
                    listem.append(y)
    return listem


def uncles(T, x):
    if T[0]==x:
        return []
    return brothers(T, root(T,x))

def aunts(T, x):
    if T[0]==x:
        return []
    return sisters(T, root(T,x)) 





        
"""T = ["a", ["b", ["e", ["j", "z"], "k"], "f", ["g", "l"]], "c", ["d", ["h", "m", "n"], "i"]]

print("a",uncles(T, "a"))
print("b",uncles(T, "b"))
print("c",uncles(T, "c"))
print("d",uncles(T, "d"))
print("e",uncles(T, "e"))
print("f",uncles(T, "f"))
print("g",uncles(T, "g"))
print("h",uncles(T, "h"))
print("i",uncles(T, "i"))
print("j",uncles(T, "j"))
print("k",uncles(T, "k"))
print("l",uncles(T, "l"))
print("m",uncles(T, "m"))
print("n",uncles(T, "n"))
print("z",uncles(T, "z"))"""
