class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int s = std::accumulate(nums.begin(), nums.end(), 0);
        if (s & 1) {
            return false;
        }
        int target = s >> 1;
        auto dp = vector<bool>(s + 1, false);
        dp[0] = true;
        
        s = 0;
        for (const auto& v: nums) {
            s += v;
            for (int i = s; i >= v; --i) {
                dp[i] = dp[i] || dp[i - v];
            }
            if (dp[target]) {
                return true;
            }
        }
        return false;
    }
};


/**
1. in <numeric>, std::accumulate(begin, end, init) is sum
2. vector<type>(n, init_val)
3. for (auto i: vector)
4. no ||= or &&= in C++
*/
