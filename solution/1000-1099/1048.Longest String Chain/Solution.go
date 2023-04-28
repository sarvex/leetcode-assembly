func longestStrChain(words []string) (ans int) {
	sort.Slice(words, func(i, j int) bool { return len(words[i]) < len(words[j]) })
	d := map[string]int{}
	for _, s := range words {
		x := 1
		for i := 0; i < len(s); i++ {
			t := s[:i] + s[i+1:]
			x = max(x, d[t]+1)
		}
		d[s] = x
		ans = max(ans, x)
	}
	return
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}