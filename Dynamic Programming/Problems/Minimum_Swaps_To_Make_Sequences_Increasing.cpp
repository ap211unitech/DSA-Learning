// Problem - https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/

#include <bits/stdc++.h>
using namespace std;

int solve(vector<int> &nums1, vector<int> &nums2, int index, bool swapped, vector<vector<int>> &dp)
{
    if (index >= nums1.size())
        return 0;

    if (dp[index][swapped] != -1)
    {
        return dp[index][swapped];
    }

    int prev1 = nums1[index - 1];
    int prev2 = nums2[index - 1];

    // IMP STEP
    if (swapped)
    {
        swap(prev1, prev2);
    }

    int ans = INT_MAX;

    if (prev1 < nums1[index] && prev2 < nums2[index])
        ans = min(ans, solve(nums1, nums2, index + 1, false, dp));

    if (prev2 < nums1[index] && prev1 < nums2[index])
        ans = min(ans, 1 + solve(nums1, nums2, index + 1, true, dp));

    return dp[index][swapped] = ans;
}

int minSwap(vector<int> &nums1, vector<int> &nums2)
{

    nums1.insert(nums1.begin(), -1);
    nums2.insert(nums2.begin(), -1);
    vector<vector<int>> dp(nums1.size() + 1, vector<int>(2, -1));

    return solve(nums1, nums2, 1, 0, dp);
}

int main()
{

    vector<int> nums1;
    vector<int> nums2;

    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int temp;
        cin >> temp;
        nums1.push_back(temp);
    }

    for (int i = 0; i < n; i++)
    {
        int temp;
        cin >> temp;
        nums2.push_back(temp);
    }

    cout << minSwap(nums1, nums2) << endl;

    return 0;
}