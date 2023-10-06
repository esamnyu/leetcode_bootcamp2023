from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen:
                return True
            else:
                seen[num] = True
        return False

if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        [1, 2, 3, 4],
        [1, 1, 2, 3],
        [7, 8, 9],
        [3, 3],
        []
    ]

    for index, test_case in enumerate(test_cases, 1):
        result = solution.containsDuplicate(test_case)
        print(f"Test Case {index}:")
        print(f"Input: {test_case}")
        print(f"Contains Duplicate: {result}\n")
