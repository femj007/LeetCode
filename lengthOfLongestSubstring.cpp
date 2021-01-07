class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s == "")
        {
            return 0;
        }
        int f[50005], be[50005];
        f[0] = 1;
        be[0] = 0;
        for (int i = 1; i < s.length(); i++)
        {
            f[i] = f[i-1] + 1;
            be[i] = be[i-1];
            for (int j = i - 1; j >= be[i-1]; j--)
            {
                if (s[j] == s[i])
                {
                    f[i] = i - j;
                    be[i] = j + 1;
                    break;
                }
            }
        }
        int maxn = 1;
        for (int i = 0; i < s.length(); i++)
        {
            if (f[i] > maxn)
            {
                maxn = f[i];
            }
        }
        return maxn;
    }
};