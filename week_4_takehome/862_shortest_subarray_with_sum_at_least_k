from collections import deque
import matplotlib.pyplot as plt

def visualize_shortest_subarray(nums, k):
    n = len(nums)
    nums = [0] + nums
    for i in range(1, n + 1):
        nums[i] += nums[i - 1]

    result = shortestSubarray(nums, k)
    print("Result:", result)

    plt.plot(nums, marker='o')
    plt.axhline(k, color='red', linestyle='--')
    plt.title('Prefix Sum Visualization')
    plt.xlabel('Index')
    plt.ylabel('Prefix Sum')
    plt.show()


def shortestSubarray(nums, k):
    n = len(nums)
    res = n + 1
    nums = [0] + nums
    for i in range(1, n + 1):
        nums[i] += nums[i - 1]
    d = deque()
    for i in range(n + 1):
        while d and nums[i] - nums[d[0]] >= k:
            res = min(res, i - d.popleft())
        while d and nums[i] <= nums[d[-1]]:
            d.pop()
        d.append(i)
    return res if res <= n else -1

nums1 = [1]
k1 = 1

nums2 = [1, 2]
k2 = 4

nums3 = [2, -1, 2]
k3 = 3

visualize_shortest_subarray(nums1, k1)
visualize_shortest_subarray(nums2, k2)
visualize_shortest_subarray(nums3, k3)