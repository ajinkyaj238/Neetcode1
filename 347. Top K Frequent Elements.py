class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums) == 1:
            return nums
        
        nums_set = set(nums)
        nums_dict = {key: 0 for key in nums_set}
        ret_lst = []
        
        for i in nums:
            nums_dict[i] += 1
                
        for j in range(k):
            ret_lst.append(max(nums_dict, key = nums_dict.get))
            nums_dict.pop(max(nums_dict, key = nums_dict.get))
            
        return 