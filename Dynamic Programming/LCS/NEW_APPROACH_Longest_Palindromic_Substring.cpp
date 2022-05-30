#include <bits/stdc++.h>
using namespace std;

int main()
{
    string s;
    cin >> s;

    int n = s.size();

    string res = "";
    int resLen = 0;

    for (int i = 0; i < n; i++)
    {
        // Odd length substring
        int l = i;
        int r = i;

        while (l >= 0 && r < n && s[l] == s[r])
        {
            if (r - l + 1 > resLen)
            {
                resLen = r - l + 1;
                res = s.substr(l, resLen);
            }
            l--;
            r++;
        }

        // Even length substring
        l = i;
        r = i + 1;

        while (l >= 0 && r < n && s[l] == s[r])
        {

            if (r - l + 1 > resLen)
            {
                resLen = r - l + 1;
                res = s.substr(l, resLen);
            }
            l--;
            r++;
        }
    }

    cout << res << endl;

    return 0;
}