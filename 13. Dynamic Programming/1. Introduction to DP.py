calls = {}

diary = [-1] * (50+1)

def fib_with_dp(n):

    if(n<=1):
        return 1 

    if(diary[n] != -1):
        return diary[n]
    
    if(n not in calls):
        calls[n] = 1
    else:
        calls[n]+=1

    fib1 = fib_with_dp(n-1)
    fib2 = fib_with_dp(n-2)

    diary[n-1] = fib1
    diary[n-2] = fib2

    ans = fib1 + fib2
    diary[n] = ans
    return ans


def fibonicci_number_recursive(n):
    if(n<=1):
        return 1
    
    if(n not in calls):
        calls[n] = 1
    else:
        calls[n]+=1
    fib1 = fibonicci_number_recursive(n-1)
    fib2 = fibonicci_number_recursive(n-2)

    return fib1 + fib2

print(fib_with_dp(50))
print(calls)
calls={}
print(fibonicci_number_recursive(50))
print(calls)

