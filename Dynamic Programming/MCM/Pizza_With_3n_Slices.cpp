// Leetcode - https://leetcode.com/problems/pizza-with-3n-slices/

#include <bits/stdc++.h>
using namespace std;

// Overall goal of this problem is to not take adjacent pizza slices and calculate maxtaken.
int solve(int index, int eindex, vector<int> &slices, int n, vector<vector<int>> &dp)
{
    if (n == 0 || index > eindex)
        return 0;

    if (dp[index][n] != -1)
    {
        return dp[index][n];
    }

    int taken = slices[index] + solve(index + 2, eindex, slices, n - 1, dp);
    int notTaken = 0 + solve(index + 1, eindex, slices, n, dp);
    return dp[index][n] = max(taken, notTaken);
}

int maxSizeSlices(vector<int> &slices)
{
    int k = slices.size();
    vector<vector<int>> dp(k + 1, vector<int>(k + 1, -1));
    int case1 = solve(0, k - 2, slices, k / 3, dp);

    vector<vector<int>> dpagain(k + 1, vector<int>(k + 1, -1));
    int case2 = solve(1, k - 1, slices, k / 3, dpagain);
    return max(case1, case2);
}

int main()
{
    vector<int> slices;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int temp;
        cin >> temp;
        slices.push_back(temp);
    }
    cout << maxSizeSlices(slices) << endl;
    return 0;
}