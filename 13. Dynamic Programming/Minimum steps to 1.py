
def min_steps_tabulation(n):
    dp = [0] *(n+1)

    dp[1] = 0

    for i in range(2,n+1):

        ans = dp[i-1] + 1

        if(i%2 ==0):
            ans = min(ans,dp[i//2] +1)
        
        if(i%3 ==0):
            ans = min(ans,dp[i//3] + 1)
        
        dp[i] = ans

    return dp[n]


def min_steps_memoization(n,memo):
    if(n==1):
        return 0
    if(memo[n]!=-1):
        return memo[n]
    
    steps = min_steps_memoization(n-1,memo)
    if(n%2==0):
        steps = min(steps,min_steps_memoization(n//2,memo))
    if(n%3==0):
        steps = min(steps,min_steps_memoization(n//3,memo))
    ans = 1 + steps

    memo[n] = ans
    return memo[n]

def min_steps_recursive(n):
    
    if(n==1):
        return 0 # Base Case
    
    steps = min_steps_recursive(n-1)

    if(n%2==0):
        steps = min(steps,min_steps_recursive(n//2))
    
    if(n%3==0):
        steps = min(steps,min_steps_recursive(n//3))

    ans = 1 + steps

    return ans

n=7
memo = [-1] * (n+1)
print(min_steps_memoization(7,memo))

print(min_steps_tabulation(10))

