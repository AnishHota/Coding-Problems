class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i,value in enumerate(nums):
            if target-value in dic:
                return [i, dic[target-value]]
            else:
                dic[value]=i
        return []
