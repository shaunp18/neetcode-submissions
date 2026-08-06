class Solution {
public:
    vector<int> countBits(int n) {
        int count = 0;
        vector<int> result = {};
        for (int i = 0; i<= n;i++){
            int j = i;
            while (j > 0){
                if (j % 2 == 1){
                    count +=1;    
                }
                j= j/2;
                
            }
            if (j == 0){
                result.push_back(count);
                count = 0;
                continue;
            }
        }
        return result;
    }
};
