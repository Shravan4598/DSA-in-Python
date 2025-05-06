"""
You have a cost matrix called cost[][], and you need to find the minimum cost 
to reach a specific position (M, N) starting from the top-left corner (0, 0).

Each cell in the matrix has a cost that you need to add up to get the total cost 
for the path you take. You can only move down, to the right, or diagonally 
down-right from any cell. 

Keep in mind that all costs are positive integers.
"""

def min_cost_path_recursive(cost, m, n):
    # Base Case
    if ( m==0 and n==0):
        return cost[0][0]

    if(m<0 or n<0):
        return float('inf')
    
    # Recursive Calls
    cost_left = min_cost_path_recursive(cost,m,n-1)
    cost_top = min_cost_path_recursive(cost,m-1,n)
    cost_diag = min_cost_path_recursive(cost,m-1,n-1)
    # our Work

    ans = cost[m][n] + min(cost_left,cost_diag,cost_top)

    return ans


def min_cost_path_memoization(cost,m,n,memo):
    # Base Case
    if(m==0 and n==0):
        return cost[0][0]

    #Out of Bounds
    if(m<0 or n<0):
        return float('inf')
    
    if(memo[m][n] !=-1):
        return memo[m][n]
    
    # Recursive Calls
    cost_left = min_cost_path_memoization(cost,m,n-1,memo)
    cost_top = min_cost_path_memoization(cost,m-1,n,memo)
    cost_diag = min_cost_path_memoization(cost,m-1,n-1,memo)

    ans = cost[m][n] + min(cost_left,cost_top,cost_diag)

    memo[m][n] = ans
    return ans

# Tabulation Approach
def min_cost_path_tabulation(cost,m,n,dp):
    
    # base case
    dp[0][0] = cost[0][0]

    for row in range(m+1):
        for col in range(n+1):
            if(row==0 and col==0):
                dp[row][col] = cost[0][0]
            else:
                cost_left = dp[row][col-1] if col>0 else float('inf')
                cost_top = dp[row-1][col] if row >0 else float('inf')
                cost_diag = dp[row-1][col-1] if ( row>0 and col>0) else float('inf')

                dp[row][col] = cost[row][col] + min(cost_diag,cost_top,cost_left)
    '''
    for col in range(n+1):
        for row in range(m+1):

    '''

    return dp[m][n]


# Test

cost_matrix = [
    [1, 2, 3],
    [4, 8, 2],
    [1, 5, 3]
]
M, N = 2, 2
memo = [ [-1 for i in range(N+1)]   for j in range(M+1) ]
dp = [ [0 for i in range(N+1)]   for j in range(M+1) ]

print(f"Minimum cost to reach ({M}, {N}) using Recursion: {min_cost_path_tabulation(cost_matrix, M, N,dp)}")



for row in dp:
    print(row)

'''
[-1, 3, 6]
[5, 9, 5]
[6, 10, 8]
'''