def wallis(s):
    import math
    n=int(s)
    r=1
    product=float(r)
    t=1
    while True:
        if t==n+1:break
        h=pow(t,2)
        product= product*(4*h/(4*h-1)) 
        t=t+1
    return(2*product)
