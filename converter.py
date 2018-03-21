def rvbhex(n):
    p=8
    hexlist=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    binlist=[0,0,0,0,0,0,0,0]
    r=''
    while p!=0:
        p=p-1
        if 2**p <= n:
            n=n-2**p
            binlist[p] = 1
    c=0
    s=0
    for i in range(0,4):
        s = s+ (2**i)*binlist[i+4]
        c=c+1
    r = '#'+ hexlist[s] 
    
    c=0
    s=0
    for i in range(0,4):
        s = s+ (2**i)*binlist[i]
        c=c+1
    r = r + hexlist[s] +"0000"
        
    print(binlist)
    return r