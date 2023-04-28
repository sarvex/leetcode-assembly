# [651. 4 键键盘](https://leetcode.cn/problems/4-keys-keyboard)

[English Version](/solution/0600-0699/0651.4%20Keys%20Keyboard/README_EN.md)

## 题目描述

<!-- 这里写题目描述 -->

<p>假设你有一个特殊的键盘包含下面的按键：</p>

<ul>
	<li><code>A</code>：在屏幕上打印一个 <code>'A'</code>。</li>
	<li><code>Ctrl-A</code>：选中整个屏幕。</li>
	<li><code>Ctrl-C</code>：复制选中区域到缓冲区。</li>
	<li><code>Ctrl-V</code>：将缓冲区内容输出到上次输入的结束位置，并显示在屏幕上。</li>
</ul>

<p>现在，<em>你可以 <strong>最多</strong> 按键 <code>n</code>&nbsp;次（使用上述四种按键），返回屏幕上最多可以显示&nbsp;<code>'A'</code>&nbsp;的个数&nbsp;</em>。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> n = 3
<strong>输出:</strong> 3
<strong>解释:</strong> 
我们最多可以在屏幕上显示三个'A'通过如下顺序按键：
A, A, A
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> n = 7
<strong>输出:</strong> 9
<strong>解释:</strong> 
我们最多可以在屏幕上显示九个'A'通过如下顺序按键：
A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 50</code></li>
</ul>

## 解法

<!-- 这里可写通用的实现逻辑 -->

**方法一：动态规划**

我们定义 $f[i][k]$ 表示前 $n+1$ 次按键后，且最后一次为第 $k$ 种按键时，屏幕上最多可以显示的 A 的个数。其中 $k$ 的取值为 $0, 1, 2, 3$，分别表示最后一次按键为 A、Ctrl+A、Ctrl+C、Ctrl+V。初始时 $f[0][0]=1$，表示第一次按键为 A，屏幕上显示一个 A。答案为 $\max(f[n-1][0], f[n-1][3])$。

考虑 $f[i][k]$，其中 $i \in [1, n-1]$：

-   当 $k=0$ 时，表示最后一次按键为 A，那么上一次按键可以为 A、Ctrl+V 中的任意一种，因此 $f[i][0]=\max(f[i-1][0], f[i-1][3]) + 1$；
-   当 $k=1$ 时，表示最后一次按键为 Ctrl+A，那么上一次按键可以为 A、Ctrl+V 中的任意一种，因此 $f[i][1]=\max(f[i-1][0], f[i-1][3])$；
-   当 $k=2$ 时，表示最后一次按键为 Ctrl+C，那么上一次按键只能为 Ctrl+A，因此 $f[i][2]=f[i-1][1]$；
-   当 $k=3$ 时，表示最后一次按键为 Ctrl+V，那么我们需要枚举上一次按 Ctrl+C 的位置 $j$，即 $f[i][3]=\max_{0 \leq j \leq i-1} f[j][2] \times (i-k+1)$。

最终答案为 $\max(f[n-1][0], f[n-1][3])$。

时间复杂度 $O(n^2)$，空间复杂度 $O(n)$。其中 $n$ 为按键次数。

**方法二：动态规划（优化）**

我们可以优化方法一中的状态定义。

我们定义 $f[i]$ 表示前 $i$ 次按键后，且最后一次按键为 A 或者 Ctrl+V 时，屏幕上最多可以显示的 A 的个数。

考虑 $f[i]$，其中 $i \in [1, n]$：

-   当最后一次按键为 A 时，有 $f[i]=f[i-1]+1$。
-   当最后一次按键为 Ctrl+V 时，我们需要枚举上一次按 Ctrl+C 的位置 $j$，即 $f[i]=\max_{0 \leq j \leq i-1} f[j] \times (i-j-1)$。

最终答案为 $f[n]$。

时间复杂度 $O(n^2)$，空间复杂度 $O(n)$。其中 $n$ 为按键次数。

<!-- tabs:start -->

### **Python3**

<!-- 这里可写当前语言的特殊实现逻辑 -->

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

<!-- 这里可写当前语言的特殊实现逻辑 -->

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
