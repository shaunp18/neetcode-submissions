class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #mylist = set(nums)
        #print(mylist)

        myList = {}

        for num in nums:
            if num in myList:
                myList[num] += 1
            else:
                myList[num] = 1
        
        top_k = []

        # Loop k times to find the k max frequencies
        for x in range(k):
            if not myList:
                break
            # Find key with max frequency
            max_key = max(myList, key=myList.get)
            top_k.append(max_key)
            del myList[max_key]  # Remove it so next max can be found

        return top_k
