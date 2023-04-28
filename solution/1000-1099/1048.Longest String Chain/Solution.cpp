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