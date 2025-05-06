

def count_balanced_bts_memoization(h,memo):
    # Base Case
    if ( h==0 or h==1):
        return 1   # For 0, we will say that a single tree of value None is possible
    
    if(memo[h] != -1):
        return memo[h]

    h1 = count_balanced_bts_memoization(h-1,memo)
    h2 = count_balanced_bts_memoization(h-2,memo)
    memo[h-1] = h1 
    memo[h-2] = h2
    ans = h1*h1 + 2*h1*h2
    memo[h] = ans
    return ans


def count_balanced_bts_recursive(h):
    # Base Case
    if ( h==0 or h==1):
        return 1   # For 0, we will say that a single tree of value None is possible
    
    h1 = count_balanced_bts_recursive(h-1)
    h2 = count_balanced_bts_recursive(h-2)

    ans = h1*h1 + 2*h1*h2

    return ans

def count_balanced_bts_tabulation(n):
    if(n<=1):
        return 1

    dp = [0] * (n+1)

    dp[0] = 1
    dp[1] = 1

    for i in range(2,n+1):
        dp[i] = dp[i-1]*dp[i-1] + 2*dp[i-1]*dp[i-2]

    return dp[n]
h=5
memo = [-1] * (h+1)
print(count_balanced_bts_tabulation(4))