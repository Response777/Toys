import numpy as np
def generator(n):
    return list(range(n,0,-1))

def Shuffle(l):
    n = len(l)//2
    for i in range(n,2*n):
        for j in range(0,2*n-i):
            l[i-j],l[i-j-1] = l[i-j-1],l[i-j]
    return l

def PerfectShuffle(l):
    r = list(range(len(l)))

    n = len(l)//2
    for i in range(n):
        r[2*i] = l[n+i]

    for i in range(n):
        r[2*i+1] = l[i]

    return r

def CycleLeader(l,pivot,m):
    n = m

    i = (2*pivot+1)%(n)
    while(i!=pivot):
        l[i],l[pivot] = l[pivot],l[i]
        i = (2*i+1)%(n)

# [lo,hi)
def Reverse(l,lo,hi):
    l[lo:hi] = l[lo:hi][::-1]

def InShuffle(_l):
    r = len(_l)
    n = r//2

    m = k = 0

    while r>0:
        l = _l[-r:]

        while(r >= 3**k - 1):
            k+=1
        k-=1;
        m = (3**k)//2

        r -= 2*m

        Reverse(l,m,-(r//2))
        Reverse(l,m,2*m)
        Reverse(l,2*m,2*m+r//2)

        for i in range(0,k):
            CycleLeader(l,3**i-1,2*m+1)
        _l[-(r+2*m):] = l[:]
        k=1;

    return _l




if __name__ == '__main__':
    array = generator(10)
    n = len(array)//2
    array[n:] = array[n:][::-1]
    print(array)


    print(Shuffle(array))

    array = generator(10)
    n = len(array)//2
    array[n:] = array[n:][::-1]
    print(PerfectShuffle(array))

    array = generator(20)
    n = len(array)//2
    array[n:] = array[n:][::-1]

    print(InShuffle(array))