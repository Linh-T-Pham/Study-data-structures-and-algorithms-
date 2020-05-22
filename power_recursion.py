def power(a,n):
    if(n == 0):
        return 1
    if(n == 1):
        return a
    
    x = power(a, n//2)
    
    if(n%2 == 0):
        return x*x
    else:
        return a*x*x


print(power(2,5))
  