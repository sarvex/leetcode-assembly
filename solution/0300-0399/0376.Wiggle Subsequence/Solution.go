func wiggleMaxLength(nums []int) int {
	f, g := 1, 1
	for i, x := range nums[1:] {
		d := x - nums[i]
		if d < 0 {
			f = max(f, g+1)
		}
		if d > 0 {
			g = max(g, f+1)
		}
	}
	return max(f, g)
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}