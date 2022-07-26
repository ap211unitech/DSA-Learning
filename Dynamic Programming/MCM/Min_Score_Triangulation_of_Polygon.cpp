// Leetcode - https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

#include <bits/stdc++.h>

using namespace std;

unordered_map<string, int> mp;
int answer(vector<int> &values, int i, int j)
{
    if (j - i == 1)
        return 0;

    string temp = to_string(i) + "-" + to_string(j);
    if (mp.find(temp) != mp.end())
    {
        return mp[temp];
    }

    int ans = INT_MAX;
    for (int k = i + 1; k < j; k++)
    {
        ans = min(ans, values[i] * values[j] * values[k] + answer(values, i, k) + answer(values, k, j));
    }
    mp[temp] = ans;
    return ans;
}

int main()
{
    vector<int> values;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int temp;
        cin >> temp;
        values.push_back(temp);
    }

    cout << answer(values, 0, n - 1) << endl;

    return 0;
}