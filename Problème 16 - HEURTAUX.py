def solve1(n): #ne fonctionne pas 
    assert solve(2**15)==26
    s=0
    a=n
    while int(a)!=0:
        b=a/10
        a=int(b)
        s+=(b-a)*10
    return(s)
    
def solve(n):
    s=0
    while n!=0:
        s+=n%10
        n=n//10
    return(s)



        

    
    