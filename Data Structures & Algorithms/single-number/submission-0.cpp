class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_map<int,int> strNums;
        for (int num : nums){
            strNums[num] += 1;
        }

        for (int num : nums){
            if (strNums[num] == 1){
                return num;
            }
        }
        return 0;
        
    }
};
