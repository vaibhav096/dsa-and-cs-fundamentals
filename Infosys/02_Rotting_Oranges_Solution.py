from collections import deque

def oranges_rotting(grid):
    """
    Calculates the minimum time to rot all oranges in the grid.
    Returns -1 if impossible.
    """
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_count = 0
    
    # 1. Initialize logic: Find all initially rotten oranges and count fresh ones
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                # Store (row, col, time_elapsed)
                queue.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh_count += 1
                
    # If there are no fresh oranges to begin with, time is 0
    if fresh_count == 0:
        return 0
        
    minutes_passed = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # Down, Up, Right, Left
    
    # 2. BFS Execution
    while queue:
        r, c, minutes_passed = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            # Check boundaries and if the neighbor is a fresh orange
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                # Make it rotten
                grid[nr][nc] = 2
                fresh_count -= 1
                # Add to queue with incremented time
                # Note: The level (time) only increases when we process the next layer
                queue.append((nr, nc, minutes_passed + 1))
    
    # 3. Final Check
    # If fresh oranges remain, it was impossible to reach them
    if fresh_count > 0:
        return -1
        
    return minutes_passed

# ---------------------------------------------------
# Driver Code
# ---------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        (
            [[2,1,1],
             [1,1,0],
             [0,1,1]], 
            4, 
            "Standard case"
        ),
        (
            [[2,1,1],
             [0,1,1],
             [1,0,1]], 
            -1, 
            "Isolated orange"
        ),
        (
            [[0,2]], 
            0, 
            "No fresh oranges"
        )
    ]
    
    print(f"{'Description':<20} | {'Expected':<10} | {'Result':<10} | {'Status'}")
    print("-" * 60)
    
    for grid_input, expected, desc in test_cases:
        # Create a deep copy because the function modifies the grid in-place
        grid_copy = [row[:] for row in grid_input]
        
        result = oranges_rotting(grid_copy)
        status = "PASSED" if result == expected else "FAILED"
        print(f"{desc:<20} | {str(expected):<10} | {str(result):<10} | {status}")
