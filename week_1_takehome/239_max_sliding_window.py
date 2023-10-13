"""
Max Sliding Window Problem:

Given an array 'nums' and an integer 'k', this algorithm returns the maximum value from each sliding window of size 'k'.

How it Works:
1. A deque (double-ended queue) named 'magic_box' is used to maintain the indices of the elements in the current window.
2. As we iterate over 'nums':
   - Remove indices from the front of the deque if they are out of the current window.
   - Remove indices from the back if the corresponding elements in 'nums' are smaller than the current element.
     This ensures that the front of the deque always contains the index of the maximum value in the current window.
   - Add the index of the current element to the back of the deque.
3. The front of the deque always contains the index of the maximum value in the current window.

The 'magic_box' deque is crucial because:
- It helps keep track of which elements are in the current window.
- By removing smaller elements from the back, it ensures we always have the maximum element of the current window readily available at the front.

Example:
For nums = [1,3,-1,-3,5,3,6,7] and k = 3, the output is [3,3,5,5,6,7].
"""
from collections import deque

def visualize_sliding_window_and_deque(nums, k):
    def visualize_window(nums, window_start, window_end, max_val):
        visual = []
        for i, num in enumerate(nums):
            box = f"[{num}]"
            if window_start <= i <= window_end:
                box = f"\033[1;34;47m{box}\033[m"  # using ANSI escape codes for color
                if num == max_val:
                    box += "*"
            visual.append(box)
        return ' '.join(visual)
    
    result = []
    magic_box = deque()
    
    for i, n in enumerate(nums):
        # Before modifications, capture the state of the deque
        before_modification = list(magic_box)
        
        while magic_box and magic_box[0] < i - k + 1:
            magic_box.popleft()
        while magic_box and nums[magic_box[-1]] < n:
            magic_box.pop()
        magic_box.append(i)
        
        if i >= k - 1:
            result.append(nums[magic_box[0]])
            # Visualize the current window and print
            print(visualize_window(nums, i - k + 1, i, nums[magic_box[0]]))
            # Print the state of the deque before and after modifications
            print(f"Magic Box (Before): {before_modification}")
            print(f"Magic Box (After) : {list(magic_box)}")
            print("-" * 50)  # separator for clarity
    
    return result

# Test with visualization
nums = [1,3,-1,-3,5,3,6,7]
k = 3
max_sliding_window_with_deque_visualization = visualize_sliding_window_and_deque(nums, k)
