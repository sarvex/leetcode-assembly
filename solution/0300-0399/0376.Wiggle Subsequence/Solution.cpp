class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        int f = 1, g = 1;
        for (int i = 1; i < nums.size(); ++i) {
            int d = nums[i] - nums[i - 1];
            if (d < 0) {
                f = max(f, g + 1);
            }
            if (d > 0) {
                g = max(g, f + 1);
            }
        }
        return max(f, g);
    }
};