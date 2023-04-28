# [376. Wiggle Subsequence](https://leetcode.com/problems/wiggle-subsequence)

[中文文档](/solution/0300-0399/0376.Wiggle%20Subsequence/README.md)

## Description

<p>A <strong>wiggle sequence</strong> is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.</p>

<ul>
	<li>For example, <code>[1, 7, 4, 9, 2, 5]</code> is a <strong>wiggle sequence</strong> because the differences <code>(6, -3, 5, -7, 3)</code> alternate between positive and negative.</li>
	<li>In contrast, <code>[1, 4, 7, 2, 5]</code> and <code>[1, 7, 4, 5, 5]</code> are not wiggle sequences. The first is not because its first two differences are positive, and the second is not because its last difference is zero.</li>
</ul>

<p>A <strong>subsequence</strong> is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.</p>

<p>Given an integer array <code>nums</code>, return <em>the length of the longest <strong>wiggle subsequence</strong> of </em><code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,7,4,9,2,5]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The entire sequence is a wiggle sequence with differences (6, -3, 5, -7, 3).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,17,5,10,13,15,10,5,16,8]
<strong>Output:</strong> 7
<strong>Explanation:</strong> There are several subsequences that achieve this length.
One is [1, 17, 10, 13, 10, 16, 8] with differences (16, -7, 3, -3, 6, -8).
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4,5,6,7,8,9]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you solve this in <code>O(n)</code> time?</p>

## Solutions

Dynamic programming.

<!-- tabs:start -->

### **Python3**

```python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        f = [[1] * 2 for _ in range(n)]
        ans = 1
        for i in range(1, n):
            for j in range(i):
                d = nums[i] - nums[j]
                if d == 0:
                    continue
                if d < 0:
                    f[i][0] = max(f[i][0], f[j][1] + 1)
                if d > 0:
                    f[i][1] = max(f[i][1], f[j][0] + 1)
            ans = max(ans, *f[i])
        return ans
```

```python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        f = g = 1
        for a, b in pairwise(nums):
            if a < b:
                f = max(f, g + 1)
            if a > b:
                g = max(g, f + 1)
        return max(f, g)
```

### **Java**

```java
class Solution {
    public int wiggleMaxLength(int[] nums) {
        int n = nums.length;
        int[][] f = new int[n][2];
        int ans = 1;
        f[0][0] = 1;
        f[0][1] = 1;
        for (int i = 1; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                int d = nums[i] - nums[j];
                if (d == 0) {
                    continue;
                }
                if (d < 0) {
                    f[i][0] = Math.max(f[i][0], f[j][1] + 1);
                }
                if (d > 0) {
                    f[i][1] = Math.max(f[i][1], f[j][0] + 1);
                }
            }
            ans = Math.max(ans, Math.max(f[i][0], f[i][1]));
        }
        return ans;
    }
}
```

```java
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
```

### **C++**

```cpp
class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        int n = nums.size();
        int f[n][2];
        memset(f, 0, sizeof(f));
        int ans = 1;
        f[0][0] = 1;
        f[0][1] = 1;
        for (int i = 1; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                int d = nums[i] - nums[j];
                if (d == 0) {
                    continue;
                }
                if (d < 0) {
                    f[i][0] = max(f[i][0], f[j][1] + 1);
                }
                if (d > 0) {
                    f[i][1] = max(f[i][1], f[j][0] + 1);
                }
            }
            ans = max({ans, f[i][0], f[i][1]});
        }
        return ans;
    }
};
```

```cpp
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
```

### **Go**

```go
func wiggleMaxLength(nums []int) int {
	n := len(nums)
	f := make([][2]int, n)
	f[0][0], f[0][1] = 1, 1
	ans := 1
	for i := 1; i < n; i++ {
		for j := 0; j < i; j++ {
			d := nums[i] - nums[j]
			if d < 0 {
				f[i][0] = max(f[i][0], f[j][1]+1)
			}
			if d > 0 {
				f[i][1] = max(f[i][1], f[j][0]+1)
			}
		}
		ans = max(ans, max(f[i][0], f[i][1]))
	}
	return ans
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
```

```go
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
```

### **TypeScript**

```ts
function wiggleMaxLength(nums: number[]): number {
    let up = 1,
        down = 1;
    for (let i = 1; i < nums.length; ++i) {
        let prev = nums[i - 1],
            cur = nums[i];
        if (cur > prev) {
            up = Math.max(up, down + 1);
        } else if (cur < prev) {
            down = Math.max(down, up + 1);
        }
    }
    return Math.max(up, down);
}
```

### **...**

```

```

<!-- tabs:end -->
