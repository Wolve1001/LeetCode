class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {} #used a dictionary(hash map), instead of using two pointers since list cannot be sorted
        for i,num in enumerate(nums): #enumerate helps keep track of both the elements and their respective indices
            complement = target - num 
            if complement in index: 
                return [index[complement],i] #if both indices found
            index[num] = i #else add the num index to the dictionary
        return [] #if no numbers sum presents the target
