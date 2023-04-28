function maxSumTwoNoOverlap(
    nums: number[],
    firstLen: number,
    secondLen: number,
): number {
    const n = nums.length;
    const s: number[] = new Array(n + 1).fill(0);
    for (let i = 0; i < n; ++i) {
        s[i + 1] = s[i] + nums[i];
    }
    let ans = 0;
    for (let i = firstLen, t = 0; i + secondLen - 1 < n; ++i) {
        t = Math.max(t, s[i] - s[i - firstLen]);
        ans = Math.max(ans, t + s[i + secondLen] - s[i]);
    }
    for (let i = secondLen, t = 0; i + firstLen - 1 < n; ++i) {
        t = Math.max(t, s[i] - s[i - secondLen]);
        ans = Math.max(ans, t + s[i + firstLen] - s[i]);
    }
    return ans;
}
