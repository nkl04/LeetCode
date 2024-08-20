class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> o;
        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            if (o.find(diff) != o.end()) {
                return {o[diff], i};
            }

            o[nums[i]] = i;
        }
        return {};
    }
};