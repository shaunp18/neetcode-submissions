class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = defaultdict(int)

        for i,num in enumerate(nums):
            complement = target - num

            if complement in s:
                return [s[complement], i]
            s[num] = i
        
        
        
        

        #set1 = set(nums)

        #for i in range(len(nums)):
        #    for j in range(i+1,len(nums)):
        #        if (nums[i] + nums[j] == target):
        #            return [i,j]
        #        j=j+1
        #i=i+1
        