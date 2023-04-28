# [1048. 最长字符串链](https://leetcode.cn/problems/longest-string-chain)

[English Version](/solution/1000-1099/1048.Longest%20String%20Chain/README_EN.md)

## 题目描述

<!-- 这里写题目描述 -->

<p>给出一个单词数组&nbsp;<code>words</code>&nbsp;，其中每个单词都由小写英文字母组成。</p>

<p>如果我们可以&nbsp;<strong>不改变其他字符的顺序&nbsp;</strong>，在 <code>word<sub>A</sub></code>&nbsp;的任何地方添加 <strong>恰好一个</strong> 字母使其变成&nbsp;<code>word<sub>B</sub></code>&nbsp;，那么我们认为&nbsp;<code>word<sub>A</sub></code>&nbsp;是&nbsp;<code>word<sub>B</sub></code>&nbsp;的 <strong>前身</strong> 。</p>

<ul>
	<li>例如，<code>"abc"</code>&nbsp;是&nbsp;<code>"abac"</code>&nbsp;的 <strong>前身</strong>&nbsp;，而&nbsp;<code>"cba"</code>&nbsp;不是&nbsp;<code>"bcad"</code>&nbsp;的 <strong>前身</strong></li>
</ul>

<p><strong>词链</strong>是单词&nbsp;<code>[word_1, word_2, ..., word_k]</code>&nbsp;组成的序列，<code>k &gt;= 1</code>，其中&nbsp;<code>word<sub>1</sub></code>&nbsp;是&nbsp;<code>word<sub>2</sub></code>&nbsp;的前身，<code>word<sub>2</sub></code>&nbsp;是&nbsp;<code>word<sub>3</sub></code>&nbsp;的前身，依此类推。一个单词通常是 <code>k == 1</code> 的 <strong>单词链</strong>&nbsp;。</p>

<p>从给定单词列表 <code>words</code> 中选择单词组成词链，返回 词链的&nbsp;<strong>最长可能长度</strong> 。<br />
&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>words = ["a","b","ba","bca","bda","bdca"]
<strong>输出：</strong>4
<strong>解释：</strong>最长单词链之一为 ["a","<u>b</u>a","b<u>d</u>a","bd<u>c</u>a"]
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<b>输入：</b>words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
<b>输出：</b>5
<b>解释：</b>所有的单词都可以放入单词链 ["xb", "xb<u>c</u>", "<u>c</u>xbc", "<u>p</u>cxbc", "pcxbc<u>f</u>"].
</pre>

<p><strong>示例&nbsp;3:</strong></p>

<pre>
<b>输入：</b>words = ["abcd","dbqca"]
<strong>输出：</strong>1
<b>解释：</b>字链["abcd"]是最长的字链之一。
["abcd"，"dbqca"]不是一个有效的单词链，因为字母的顺序被改变了。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 16</code></li>
	<li><code>words[i]</code>&nbsp;仅由小写英文字母组成。</li>
</ul>

## 解法

<!-- 这里可写通用的实现逻辑 -->

**方法一：排序 + 哈希表**

根据题目描述，字符串链中的单词必须按照长度递增的顺序排列。因此，我们首先对数组 `words` 中的字符串按照长度进行升序排序。在排好序的数组中，如果字符串 $a$ 是字符串 $b$ 的前身，那么字符串 $a$ 的长度一定是字符串 $b$ 的长度减去 $1$。

我们可以使用哈希表 $d$ 存储排好序的数组中的每个字符串的最长字符串链长度。

接下来，遍历数组 `words` 中的每个字符串 $s$，计算出它的所有前身字符串 $t$，每一个前身字符串 $t$ 是将字符串 $s$ 中的一个字符删除后得到的。如果哈希表中存在字符串 $t$，那么我们就能够用 $d[t] + 1$ 更新 $d[s]$，即 $d[s] = \max(d[s], d[t] + 1)$。然后我们更新答案为所有 $d[s]$ 中的最大值。

遍历结束后，返回答案即可。

时间复杂度 $(n \times (\log n + m^2))$，空间复杂度 $O(n)$。其中 $n$ 和 $m$ 分别是单词数组 `words` 的长度和单词的最大长度。本题中 $n \leq 1000$, $m \leq 16$。

<!-- tabs:start -->

### **Python3**

<!-- 这里可写当前语言的特殊实现逻辑 -->

```python
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def check(s: str, t: str) -> bool:
            m, n = len(s), len(t)
            i = j = 0
            while i < m and j < n:
                if s[i] == t[j]:
                    i += 1
                j += 1
            return i == m

        words.sort(key=len)
        f = [1] * len(words)
        d = defaultdict(list)
        for i, w in enumerate(words):
            for j in d[len(w) - 1]:
                if check(words[j], w):
                    f[i] = max(f[i], f[j] + 1)
            d[len(w)].append(i)
        return max(f)
```

```python
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        d = defaultdict(int)
        ans = 0
        for s in words:
            x = 1
            for i in range(len(s)):
                t = s[:i] + s[i + 1:]
                x = max(x, d[t] + 1)
            d[s] = x
            ans = max(ans, x)
        return ans
```

### **Java**

<!-- 这里可写当前语言的特殊实现逻辑 -->

```java
class Solution {
    public int longestStrChain(String[] words) {
        Arrays.sort(words, Comparator.comparingInt(String::length));
        int n = words.length;
        int[] f = new int[n];
        Arrays.fill(f, 1);
        List<Integer>[] g = new List[17];
        Arrays.setAll(g, k -> new ArrayList<>());
        int ans = 1;
        for (int i = 0; i < n; ++i) {
            String w = words[i];
            for (int j : g[w.length() - 1]) {
                if (check(words[j], w)) {
                    f[i] = Math.max(f[i], f[j] + 1);
                    ans = Math.max(ans, f[i]);
                }
            }
            g[w.length()].add(i);
        }
        return ans;
    }

    private boolean check(String s, String t) {
        int m = s.length(), n = t.length();
        int i = 0, j = 0;
        while (i < m && j < n) {
            if (s.charAt(i) == t.charAt(j)) {
                ++i;
            }
            ++j;
        }
        return i == m;
    }
}
```

```java
class Solution {
    public int longestStrChain(String[] words) {
        Arrays.sort(words, Comparator.comparingInt(String::length));
        Map<String, Integer> d = new HashMap<>();
        int ans = 0;
        for (String s : words) {
            int x = 0;
            for (int i = 0; i < s.length(); ++i) {
                String t = s.substring(0, i) + s.substring(i + 1);
                x = Math.max(x, d.getOrDefault(t, 0) + 1);
            }
            d.put(s, x);
            ans = Math.max(ans, x);
        }
        return ans;
    }
}
```

### **C++**

```cpp
class Solution {
public:
    int longestStrChain(vector<string>& words) {
        sort(words.begin(), words.end(), [](auto& a, auto& b) { return a.size() < b.size(); });
        int n = words.size();
        int f[n];
        vector<int> g[17];
        int ans = 1;
        auto check = [](string& s, string& t) -> bool {
            int m = s.size(), n = t.size();
            int i = 0, j = 0;
            while (i < m && j < n) {
                if (s[i] == t[j]) {
                    ++i;
                }
                ++j;
            }
            return i == m;
        };
        for (int i = 0; i < n; ++i) {
            f[i] = 1;
            auto w = words[i];
            for (int j : g[w.size() - 1]) {
                if (check(words[j], w)) {
                    f[i] = max(f[i], f[j] + 1);
                    ans = max(ans, f[i]);
                }
            }
            g[w.size()].push_back(i);
        }
        return ans;
    }
};
```

```cpp
class Solution {
public:
    int longestStrChain(vector<string>& words) {
        sort(words.begin(), words.end(), [](auto& a, auto& b) { return a.size() < b.size(); });
        int ans = 0;
        unordered_map<string, int> d;
        for (auto& s : words) {
            int x = 1;
            for (int i = 0; i < s.size(); ++i) {
                string t = s.substr(0, i) + s.substr(i + 1);
                x = max(x, d[t] + 1);
            }
            d[s] = x;
            ans = max(ans, x);
        }
        return ans;
    }
};
```

### **Go**

```go
func longestStrChain(words []string) int {
	sort.Slice(words, func(i, j int) bool { return len(words[i]) < len(words[j]) })
	n := len(words)
	f := make([]int, n)
	g := [17][]int{}
	ans := 1
	check := func(s, t string) bool {
		m, n := len(s), len(t)
		i, j := 0, 0
		for i < m && j < n {
			if s[i] == t[j] {
				i++
			}
			j++
		}
		return i == m
	}
	for i, w := range words {
		f[i] = 1
		for _, j := range g[len(w)-1] {
			if check(words[j], w) {
				f[i] = max(f[i], f[j]+1)
				ans = max(ans, f[i])
			}
		}
		g[len(w)] = append(g[len(w)], i)
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
```

### **TypeScript**

```ts
function longestStrChain(words: string[]): number {
    words.sort((a, b) => a.length - b.length);
    let ans = 1;
    const n = words.length;
    const f: number[] = new Array(n).fill(1);
    const g: number[][] = new Array(17).fill(0).map(() => []);
    const check = (s: string, t: string): boolean => {
        const m = s.length;
        const n = t.length;
        let i = 0;
        let j = 0;
        while (i < m && j < n) {
            if (s[i] === t[j]) {
                ++i;
            }
            ++j;
        }
        return i === m;
    };
    for (let i = 0; i < n; ++i) {
        const w = words[i];
        for (const j of g[w.length - 1]) {
            if (check(words[j], w)) {
                f[i] = Math.max(f[i], f[j] + 1);
                ans = Math.max(ans, f[i]);
            }
        }
        g[w.length].push(i);
    }
    return ans;
}
```

```ts
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
```

### **...**

```

```

<!-- tabs:end -->
