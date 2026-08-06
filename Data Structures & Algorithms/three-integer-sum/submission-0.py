class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r = []

        nums.sort()
        for i,num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]: 
                continue
            
            complement_1 = 0 - num
            s = defaultdict(int)

            for j in range(i+1,len(nums)):
                complement_2 = complement_1 - nums[j]
                
                if complement_2 in s:
                    triplet = [nums[i], nums[j], complement_2]
                    triplet.sort()  # sort before checking duplicates
                    if triplet not in r:  # avoid duplicates in results
                        r.append(triplet)
                
                s[nums[j]] = j
        return r

