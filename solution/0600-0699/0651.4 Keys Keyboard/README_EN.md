# [651. 4 Keys Keyboard](https://leetcode.com/problems/4-keys-keyboard)

[中文文档](/solution/0600-0699/0651.4%20Keys%20Keyboard/README.md)

## Description

<p>Imagine you have a special keyboard with the following keys:</p>

<ul>
	<li>A: Print one <code>&#39;A&#39;</code> on the screen.</li>
	<li>Ctrl-A: Select the whole screen.</li>
	<li>Ctrl-C: Copy selection to buffer.</li>
	<li>Ctrl-V: Print buffer on screen appending it after what has already been printed.</li>
</ul>

<p>Given an integer n, return <em>the maximum number of </em><code>&#39;A&#39;</code><em> you can print on the screen with <strong>at most</strong> </em><code>n</code><em> presses on the keys</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> We can at most get 3 A&#39;s on screen by pressing the following key sequence:
A, A, A
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 7
<strong>Output:</strong> 9
<strong>Explanation:</strong> We can at most get 9 A&#39;s on screen by pressing following key sequence:
A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 50</code></li>
</ul>

## Solutions

<!-- tabs:start -->

### **Python3**

```python
class Solution:
    def maxA(self, n: int) -> int:
        f = [[0] * 4 for _ in range(n)]
        f[0][0] = 1
        for i in range(1, n):
            f[i][0] = max(f[i - 1][0], f[i - 1][3]) + 1
            f[i][1] = max(f[i - 1][0], f[i - 1][3])
            f[i][2] = f[i - 1][1]
            for j in range(i):
                f[i][3] = max(f[i][3], f[j][2] * (i - j + 1))
        return max(f[-1][0], f[-1][3])
```

```python
class Solution:
    def maxA(self, n: int) -> int:
        f = [0] * (n + 1)
        for i in range(1, n + 1):
            f[i] = f[i - 1] + 1
            for j in range(2, i):
                f[i] = max(f[i], f[j - 2] * (i - j + 1))
        return f[n]
```

### **Java**

```java
class Solution {
    public int maxA(int n) {
        int[][] f = new int[n][4];
        f[0][0] = 1;
        for (int i = 1; i < n; ++i) {
            f[i][0] = Math.max(f[i - 1][0], f[i - 1][3]) + 1;
            f[i][1] = Math.max(f[i - 1][0], f[i - 1][3]);
            f[i][2] = f[i - 1][1];
            for (int j = 0; j < i; ++j) {
                f[i][3] = Math.max(f[i][3], f[j][2] * (i - j + 1));
            }
        }
        return Math.max(f[n - 1][0], f[n - 1][3]);
    }
}
```

```java
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
```

### **C++**

```cpp
class Solution {
public:
    int maxA(int n) {
        int f[n][4];
        memset(f, 0, sizeof(f));
        f[0][0] = 1;
        for (int i = 1; i < n; ++i) {
            f[i][0] = max(f[i - 1][0], f[i - 1][3]) + 1;
            f[i][1] = max(f[i - 1][0], f[i - 1][3]);
            f[i][2] = f[i - 1][1];
            for (int j = 0; j < i; ++j) {
                f[i][3] = max(f[i][3], f[j][2] * (i - j + 1));
            }
        }
        return max(f[n - 1][0], f[n - 1][3]);
    }
};
```

```cpp
class Solution {
public:
    int maxA(int n) {
        int f[n + 1];
        memset(f, 0, sizeof(f));
        for (int i = 1; i <= n; ++i) {
            f[i] = f[i - 1] + 1;
            for (int j = 2; j < i; ++j) {
                f[i] = max(f[i], f[j - 2] * (i - j + 1));
            }
        }
        return f[n];
    }
};
```

### **Go**

```go
func maxA(n int) int {
	f := make([][4]int, n)
	f[0][0] = 1
	for i := 1; i < n; i++ {
		f[i][0] = max(f[i-1][0], f[i-1][3]) + 1
		f[i][1] = max(f[i-1][0], f[i-1][3])
		f[i][2] = f[i-1][1]
		for j := 0; j < i; j++ {
			f[i][3] = max(f[i][3], f[j][2]*(i-j+1))
		}
	}
	return max(max(f[n-1][0], f[n-1][1]), max(f[n-1][2], f[n-1][3]))
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
```

```go
func maxA(n int) int {
	f := make([]int, n+1)
	for i := 1; i <= n; i++ {
		f[i] = f[i-1] + 1
		for j := 2; j < i; j++ {
			f[i] = max(f[i], f[j-2]*(i-j+1))
		}
	}
	return f[n]
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
```

### **...**

```

```

<!-- tabs:end -->
