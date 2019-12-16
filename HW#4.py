Q1

def mk_wd(balance):
    
    
    
    def withdraw(M):
        nonlocal balance    
        balance-=M
        if(balance<0):
            return "insufficient funds" 
        return  balance
    return withdraw
rem=mk_wd(100)
print(rem(10))
print(rem(20))
print(rem(40))
print(rem(100))

Q2
def rm_all(elem, lst):
    x=[]
    for a in lst:
        if(elem!=a):
            x.append(a)
    return x


x = [3, 1, 2, 1, 5, 1, 1, 7]
print(rm_all (1, x))

Q3
def add_many(x, elem, lst):
    for x in range(0,x):
        lst.append(elem)
    return lst


lst = [1, 2, 4, 2, 1]
print(add_many (2, 5, lst) )

Q4
def f (suits, numbers):
    
    z=[[] for i in range(len(suits)*len(numbers))]
    count=0
    for y in range(0,len(suits)):
        for t in range(0,len(numbers)):
            
            z[count]=suits[y],numbers[t]
            count+=1


return z


print(f(['S', 'C'], [1, 2, 3]))
print(f(['S', 'C'], [3, 2, 1]))

Q5
def mrg(ls1, ls2):
    ls=ls1+ls2
    sorted=[]
    def srt(ls):
        x=min(ls)
        ls.remove(x)
        sorted.append(x)
        if not ls:
            return sorted
        
        return srt(ls)
    return srt(ls)
print(mrg ([1, 3, 5], [2, 4, 6]))

Q6
def fltn(lst):
    
    if type(lst) != list:
        
        return [lst]
    else:
        
        
        return sum([fltn(elem) for elem in lst],[])



x =  [[1, [2, 3]], 4, [5, 6]]
print(fltn (x))

Q7


def tem(lst):
    if type(lst) != list:
        
        return [lst]
    else:
        return sum([tem(elem) for elem in lst],[])
def chk_elm(lst,n):
    lst=tem(lst)
    for i in lst:
        if(i==n):
            return True
    return False



x =  [[1, [2, 3]], 4, [5, 6]]
print(chk_elm (x,4))

Q8
def sym(l):
    if(len(l)==0 or len(l)==1):
        return True
    if(l[0]==l[-1]):
        l.remove(l[0])
        l.remove(l[-1])
    if(len(l)==2 and l[0]!=l[1]):
        return False
    
    return sym(l)

print(sym ([1]))
print(sym ([1, 4, 5, 1]))
print(sym ([1, 4, 4, 1]))
print(sym (['l', 'o', 'l']))

Q9
def add(i,lst):
    return i+lst
def sub(i,lst):
    return i-lst
def mul(i,lst):
    return i*lst
def fld (lst, g, i):
    i=g(i,lst[0])
    lst.remove(lst[0])
    if len(lst)==1:
        return g(i,lst[0])
    
    return fld(lst,g,i)


s=[3,2,1]
print(fld (s, mul, 1))

Q10
def create_2d_arr(rows, columns):
    i=[]
    b=[]
    for column in range(0,columns):
        i.append('-')
    for row in range(0,rows):
        b.append(i)
    return b




print(create_2d_arr (3, 5))

