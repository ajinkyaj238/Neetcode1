class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in nums:
            if i < target:
                for j in nums:
                    if j != i and j < target:
                        if i + j == target:
                            return [i, j]
        