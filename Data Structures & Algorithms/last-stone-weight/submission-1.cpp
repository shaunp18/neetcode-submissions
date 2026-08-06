class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        std::priority_queue<int> s(stones.begin(), stones.end());

        while (s.size() > 1){
            int a = s.top();
            s.pop();
            int b = s.top();
            s.pop();
            
            if (a != b){
                s.push(a-b);
            }
        }
        if (s.size() == 1){
            return s.top();
        }
        else{
            return 0;
        }
    }
    
};
