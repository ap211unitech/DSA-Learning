#include <bits/stdc++.h>

using namespace std;

int main()
{
    string s;
    cin >> s;
    unordered_map<char, int> mp;
    int n = s.size();
    int i = 0;
    int j = 0;
    int res = 0;
    while (i < n)
    {
        if (mp.find(s[i]) == mp.end())
        {
            mp[s[i]]++;
            int len = (i - j + 1);
            res += (len) ;
            // cout<<res<<endl;
        }
        else
        {
            while (j < i)
            {
                mp.erase(s[j]);
                if (s[j] == s[i])
                {
                    int len = (i - j);
                    res += (len) ;
                    j++;
                    // cout<<j<<" "<<res<<" "<<len<<endl;
                    break;
                }
                j++;
            }
            mp[s[i]]++;
        }
        i++;
        // cout << res << endl;
    }
    cout << res << endl;
    return 0;
}