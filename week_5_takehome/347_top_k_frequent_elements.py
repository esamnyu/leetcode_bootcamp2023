from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each element in nums
        freq_map = Counter(nums)

        # Use a heap to store the frequency and element
        # Python's heapq module implements a min-heap, so we use negative frequencies
        # to simulate a max-heap based on frequency
        heap = []

        # Build the heap of size k
        for num, freq in freq_map.items():
            heapq.heappush(heap, (-freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        # Extract the top k elements from the heap
        top_k = [heapq.heappop(heap)[1] for _ in range(k)]

        return top_k
