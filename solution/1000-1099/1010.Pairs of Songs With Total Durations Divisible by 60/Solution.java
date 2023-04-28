class Solution {
    public int numPairsDivisibleBy60(int[] time) {
        int[] cnt = new int[501];
        int ans = 0;
        for (int t : time) {
            int s = 60;
            for (int i = 0; i < 17; ++i) {
                if (s - t >= 0 && s - t < cnt.length) {
                    ans += cnt[s - t];
                }
                s += 60;
            }
            cnt[t]++;
        }
        return ans;
    }
}