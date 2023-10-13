import matplotlib.pyplot as plt
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        result = 0
        max_l, max_r = l, r  # Track the walls that produce the max area
        
        # Visualization setup
        plt.figure(figsize=(10, 6))
        plt.bar(range(len(height)), height, color='lightblue')
        plt.title("Visualization of Two-Pointer Approach")
        
        while l < r:
            # Calculate and compare the area
            area = (r - l) * min(height[l], height[r])
            if area > result:
                result = area
                max_l, max_r = l, r  # Update the walls with the new max area
                
            # Visualization update
            plt.clf()  # Clear the current figure
            plt.bar(range(len(height)), height, color='lightblue')
            plt.bar(l, height[l], color='red')
            plt.bar(r, height[r], color='green')
            
            # Display current area as a rectangle
            plt.fill_between(range(l, r+1), 0, min(height[l], height[r]), color='yellow', alpha=0.3)
            
            plt.pause(0.5)
            
            # Trick: Move the pointer pointing to the shorter line inwards
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        # Display the frame with the maximum area
        plt.clf()
        plt.bar(range(len(height)), height, color='lightblue')
        plt.bar(max_l, height[max_l], color='red')
        plt.bar(max_r, height[max_r], color='green')
        plt.fill_between(range(max_l, max_r+1), 0, min(height[max_l], height[max_r]), color='yellow', alpha=0.3)
        plt.title(f"Maximum Area: {result}")
        
        plt.show()
        return result

# Example
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
solution = Solution()
print(solution.maxArea(heights))
