def numIslands(grid):
    # Number of rows and columns in the grid
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])

    # Function to perform DFS from a given cell
    def dfs(r, c):
        # Base condition: if the current cell is out of bounds or is water ('0'),
        # we return and do not continue the DFS from this cell.
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return

        # Mark the current cell as visited by setting it to '0' (water)
        grid[r][c] = '0'

        # Continue DFS in all four directions (up, down, left, right)
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    # Count to keep track of the number of islands
    count = 0

    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If the cell is land ('1'), it is a part of an island.
            if grid[r][c] == '1':
                # Increment the count of islands
                count += 1
                # Perform DFS to mark all cells of this island
                dfs(r, c)

    # Return the total count of islands found
    return count

# Example usage
grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
print(numIslands(grid))
