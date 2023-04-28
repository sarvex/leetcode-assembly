class Solution {
    public int maxA(int n) {
        int[] f = new int[n + 1];
        for (int i = 1; i <= n; ++i) {
            f[i] = f[i - 1] + 1;
            for (int j = 2; j < i; ++j) {
                f[i] = Math.max(f[i], f[j - 2] * (i - j + 1));
            }
        }
        return f[n];
    }
}