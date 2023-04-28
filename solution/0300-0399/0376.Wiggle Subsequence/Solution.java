class Solution {
    public int wiggleMaxLength(int[] nums) {
        int f = 1, g = 1;
        for (int i = 1; i < nums.length; ++i) {
            int d = nums[i] - nums[i - 1];
            if (d < 0) {
                f = Math.max(f, g + 1);
            }
            if (d > 0) {
                g = Math.max(g, f + 1);
            }
        }
        return Math.max(f, g);
    }
}