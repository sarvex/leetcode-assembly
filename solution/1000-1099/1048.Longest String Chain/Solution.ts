function longestStrChain(words: string[]): number {
    words.sort((a, b) => a.length - b.length);
    let ans = 0;
    const d: Map<string, number> = new Map();
    for (const s of words) {
        let x = 1;
        for (let i = 0; i < s.length; ++i) {
            const t = s.slice(0, i) + s.slice(i + 1);
            x = Math.max(x, (d.get(t) || 0) + 1);
        }
        d.set(s, x);
        ans = Math.max(ans, x);
    }
    return ans;
}
