def minPathSum(grid):
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])

    # Create a 2D dp array with the same dimensions as grid
    dp = [[0] * n for _ in range(m)]
    
    # Initialize the value at (0, 0)
    dp[0][0] = grid[0][0]

    # Initialize the first column
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    # Initialize the first row
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # Compute minPathSum for each cell
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]

# Test
grid1 = [[1,3,1],[1,5,1],[4,2,1]]
print(minPathSum(grid1))  # Expected output: 7

grid2 = [[1,2,3],[4,5,6]]
print(minPathSum(grid2))  # Expected output: 12
