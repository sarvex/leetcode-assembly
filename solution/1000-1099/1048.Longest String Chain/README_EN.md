# [1048. Longest String Chain](https://leetcode.com/problems/longest-string-chain)

[中文文档](/solution/1000-1099/1048.Longest%20String%20Chain/README.md)

## Description

<p>You are given an array of <code>words</code> where each word consists of lowercase English letters.</p>

<p><code>word<sub>A</sub></code> is a <strong>predecessor</strong> of <code>word<sub>B</sub></code> if and only if we can insert <strong>exactly one</strong> letter anywhere in <code>word<sub>A</sub></code> <strong>without changing the order of the other characters</strong> to make it equal to <code>word<sub>B</sub></code>.</p>

<ul>
	<li>For example, <code>&quot;abc&quot;</code> is a <strong>predecessor</strong> of <code>&quot;ab<u>a</u>c&quot;</code>, while <code>&quot;cba&quot;</code> is not a <strong>predecessor</strong> of <code>&quot;bcad&quot;</code>.</li>
</ul>

<p>A <strong>word chain</strong><em> </em>is a sequence of words <code>[word<sub>1</sub>, word<sub>2</sub>, ..., word<sub>k</sub>]</code> with <code>k &gt;= 1</code>, where <code>word<sub>1</sub></code> is a <strong>predecessor</strong> of <code>word<sub>2</sub></code>, <code>word<sub>2</sub></code> is a <strong>predecessor</strong> of <code>word<sub>3</sub></code>, and so on. A single word is trivially a <strong>word chain</strong> with <code>k == 1</code>.</p>

<p>Return <em>the <strong>length</strong> of the <strong>longest possible word chain</strong> with words chosen from the given list of </em><code>words</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;a&quot;,&quot;b&quot;,&quot;ba&quot;,&quot;bca&quot;,&quot;bda&quot;,&quot;bdca&quot;]
<strong>Output:</strong> 4
<strong>Explanation</strong>: One of the longest word chains is [&quot;a&quot;,&quot;<u>b</u>a&quot;,&quot;b<u>d</u>a&quot;,&quot;bd<u>c</u>a&quot;].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;xbc&quot;,&quot;pcxbcf&quot;,&quot;xb&quot;,&quot;cxbc&quot;,&quot;pcxbc&quot;]
<strong>Output:</strong> 5
<strong>Explanation:</strong> All the words can be put in a word chain [&quot;xb&quot;, &quot;xb<u>c</u>&quot;, &quot;<u>c</u>xbc&quot;, &quot;<u>p</u>cxbc&quot;, &quot;pcxbc<u>f</u>&quot;].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;abcd&quot;,&quot;dbqca&quot;]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The trivial word chain [&quot;abcd&quot;] is one of the longest word chains.
[&quot;abcd&quot;,&quot;dbqca&quot;] is not a valid word chain because the ordering of the letters is changed.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 16</code></li>
	<li><code>words[i]</code> only consists of lowercase English letters.</li>
</ul>

## Solutions

**Solution 1: Sorting + Hash Table**

According to the description of the problem, the words in the string chain must be sorted in order of increasing length. Therefore, we first sort the strings in the array `words` in ascending order by length. In the sorted array, if string $a$ is the predecessor of string $b$, then the length of string $a$ must be the length of string $b$ minus $1$.

We can use the hash table $d$ to store the longest string chain length of each string in the sorted array.

Next, traverse each string $s$ in the array `words` and calculate all predecessor strings $t$. Each predecessor string $t$ is obtained by deleting one character from string $s$. If string $t$ exists in the hash table, then we can update $d[s]$ with $d[t] + 1$, that is, $d[s] = \max(d[s], d[t] + 1)$. Then we update the answer to the maximum value of all $d[s]$.

After the traversal is over, return the answer.

The time complexity is $(n \times (\log n + m^2))$, and the space complexity is $O(n)$. Where $n$ and $m$ are the length of the word array `words` and the maximum length of the word respectively. In this question, $n \leq 1000$, $m \leq 16$.

<!-- tabs:start -->

### **Python3**

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
