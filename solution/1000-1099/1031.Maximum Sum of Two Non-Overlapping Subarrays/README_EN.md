# [1031. Maximum Sum of Two Non-Overlapping Subarrays](https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays)

[中文文档](/solution/1000-1099/1031.Maximum%20Sum%20of%20Two%20Non-Overlapping%20Subarrays/README.md)

## Description

<p>Given an integer array <code>nums</code> and two integers <code>firstLen</code> and <code>secondLen</code>, return <em>the maximum sum of elements in two non-overlapping <strong>subarrays</strong> with lengths </em><code>firstLen</code><em> and </em><code>secondLen</code>.</p>

<p>The array with length <code>firstLen</code> could occur before or after the array with length <code>secondLen</code>, but they have to be non-overlapping.</p>

<p>A <strong>subarray</strong> is a <strong>contiguous</strong> part of an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
<strong>Output:</strong> 20
<strong>Explanation:</strong> One choice of subarrays is [9] with length 1, and [6,5] with length 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2
<strong>Output:</strong> 29
<strong>Explanation:</strong> One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3
<strong>Output:</strong> 31
<strong>Explanation:</strong> One choice of subarrays is [5,6,0,9] with length 4, and [0,3,8] with length 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= firstLen, secondLen &lt;= 1000</code></li>
	<li><code>2 &lt;= firstLen + secondLen &lt;= 1000</code></li>
	<li><code>firstLen + secondLen &lt;= nums.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

## Solutions

**Solution 1: Prefix Sum + Enumeration**

First, we preprocess the prefix sum array $s$ of the array `nums`, where $s[i]$ indicates the sum of the first $i$ elements in `nums`.

Then, we enumerate in two cases:

Suppose $firstLen$ elements of the subarray are on the left side of the $secondLen$ elements of the subarray, then we can enumerate the left endpoint $i$ of the $secondLen$ elements of the subarray, use the variable $t$ to maintain the maximum sum of the left $firstLen$ elements of the subarray, then the current maximum sum is $t + s[i + secondLen] - s[i]$. Where $s[i + secondLen] - s[i]$ represents the sum of the $secondLen$ elements of the subarray. After enumerating all $i$, we get the maximum sum of the first case.

Suppose the $secondLen$ elements of the subarray are on the left side of the $firstLen$ elements of the subarray, then we can enumerate the left endpoint $i$ of the $firstLen$ elements of the subarray, use the variable $t$ to maintain the maximum sum of the left $secondLen$ elements of the subarray, then the current maximum sum is $t + s[i + firstLen] - s[i]$. Where $s[i + firstLen] - s[i]$ represents the sum of the $firstLen$ elements of the subarray. After enumerating all $i$, we get the maximum sum of the second case.

Take the maximum value of the two cases as the answer.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Where $n$ is the length of the array `nums`.

<!-- tabs:start -->

### **Python3**

```python
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial=0))
        ans = t = 0
        i = firstLen
        while i + secondLen - 1 < n:
            t = max(t, s[i] - s[i - firstLen])
            ans = max(ans, t + s[i + secondLen] - s[i])
            i += 1
        t = 0
        i = secondLen
        while i + firstLen - 1 < n:
            t = max(t, s[i] - s[i - secondLen])
            ans = max(ans, t + s[i + firstLen] - s[i])
            i += 1
        return ans
```

```python
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        def f(a: int, b: int) -> int:
            ans = t = 0
            i = a
            while i + b - 1 < n:
                t = max(t, s[i] - s[i - a])
                ans = max(ans, t + s[i + b] - s[i])
                i += 1
            return ans

        n = len(nums)
        s = list(accumulate(nums, initial=0))
        return max(f(firstLen, secondLen), f(secondLen, firstLen))
```

### **Java**

```java
class Solution {
    public int maxSumTwoNoOverlap(int[] nums, int firstLen, int secondLen) {
        int n = nums.length;
        int[] s = new int[n + 1];
        for (int i = 0; i < n; ++i) {
            s[i + 1] = s[i] + nums[i];
        }
        int ans = 0;
        for (int i = firstLen, t = 0; i + secondLen - 1 < n; ++i) {
            t = Math.max(t, s[i] - s[i - firstLen]);
            ans = Math.max(ans, t + s[i + secondLen] - s[i]);
        }
        for (int i = secondLen, t = 0; i + firstLen - 1 < n; ++i) {
            t = Math.max(t, s[i] - s[i - secondLen]);
            ans = Math.max(ans, t + s[i + firstLen] - s[i]);
        }
        return ans;
    }
}
```

```java
class Solution {
    private int[] s;
    private int n;

    public int maxSumTwoNoOverlap(int[] nums, int firstLen, int secondLen) {
        n = nums.length;
        s = new int[n + 1];
        for (int i = 0; i < n; ++i) {
            s[i + 1] = s[i] + nums[i];
        }
        return Math.max(f(firstLen, secondLen), f(secondLen, firstLen));
    }

    private int f(int a, int b) {
        int ans = 0;
        for (int i = a, t = 0; i + b - 1 < n; ++i) {
            t = Math.max(t, s[i] - s[i - a]);
            ans = Math.max(ans, t + s[i + b] - s[i]);
        }
        return ans;
    }
}
```

### **C++**

```cpp
class Solution {
public:
    int maxSumTwoNoOverlap(vector<int>& nums, int firstLen, int secondLen) {
        int n = nums.size();
        vector<int> s(n + 1);
        for (int i = 0; i < n; ++i) {
            s[i + 1] = s[i] + nums[i];
        }
        int ans = 0;
        for (int i = firstLen, t = 0; i + secondLen - 1 < n; ++i) {
            t = max(t, s[i] - s[i - firstLen]);
            ans = max(ans, t + s[i + secondLen] - s[i]);
        }
        for (int i = secondLen, t = 0; i + firstLen - 1 < n; ++i) {
            t = max(t, s[i] - s[i - secondLen]);
            ans = max(ans, t + s[i + firstLen] - s[i]);
        }
        return ans;
    }
};
```

```cpp
class Solution {
public:
    int maxSumTwoNoOverlap(vector<int>& nums, int firstLen, int secondLen) {
        int n = nums.size();
        vector<int> s(n + 1);
        for (int i = 0; i < n; ++i) {
            s[i + 1] = s[i] + nums[i];
        }
        auto f = [&](int a, int b) -> int {
            int ans = 0;
            for (int i = a, t = 0; i + b - 1 < n; ++i) {
                t = max(t, s[i] - s[i - a]);
                ans = max(ans, t + s[i + b] - s[i]);
            }
            return ans;
        };
        return max(f(firstLen, secondLen), f(secondLen, firstLen));
    }
};
```

### **Go**

```go
func maxSumTwoNoOverlap(nums []int, firstLen int, secondLen int) (ans int) {
	n := len(nums)
	s := make([]int, n+1)
	for i, x := range nums {
		s[i+1] = s[i] + x
	}
	for i, t := firstLen, 0; i+secondLen-1 < n; i++ {
		t = max(t, s[i]-s[i-firstLen])
		ans = max(ans, t+s[i+secondLen]-s[i])
	}
	for i, t := secondLen, 0; i+firstLen-1 < n; i++ {
		t = max(t, s[i]-s[i-secondLen])
		ans = max(ans, t+s[i+firstLen]-s[i])
	}
	return
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
```

```go
func maxSumTwoNoOverlap(nums []int, firstLen int, secondLen int) (ans int) {
	n := len(nums)
	s := make([]int, n+1)
	for i, x := range nums {
		s[i+1] = s[i] + x
	}
	f := func(a, b int) (ans int) {
		for i, t := a, 0; i+b-1 < n; i++ {
			t = max(t, s[i]-s[i-a])
			ans = max(ans, t+s[i+b]-s[i])
		}
		return
	}
	return max(f(firstLen, secondLen), f(secondLen, firstLen))
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
```

```ts
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
    const f = (a: number, b: number): number => {
        let ans = 0;
        for (let i = a, t = 0; i + b - 1 < n; ++i) {
            t = Math.max(t, s[i] - s[i - a]);
            ans = Math.max(ans, t + s[i + b] - s[i]);
        }
        return ans;
    };
    return Math.max(f(firstLen, secondLen), f(secondLen, firstLen));
}
```

### **...**

```

```

<!-- tabs:end -->
