// Leetcode - https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

#include <bits/stdc++.h>

using namespace std;

struct compare
{
    bool operator()(vector<int> &a, vector<int> &b)
    {
        return a[0] > b[0];
    }
};

vector<int> answer(vector<vector<int>> &a, int k, int n)
{
    int range = INT_MAX;
    int start = INT_MAX;
    int end = INT_MIN;

    priority_queue<vector<int>, vector<vector<int>>, compare> mnheap;

    int mxval = INT_MIN;
    for (int i = 0; i < k; i++)
    {
        vector<int> temp = {a[i][0], i, 0};
        mnheap.push(temp);
        mxval = max(mxval, a[i][0]);
    }

    while (true)
    {

        vector<int> mnv = mnheap.top();
        mnheap.pop();
        if (range > mxval - mnv[0] + 1)
        {
            range = mxval - mnv[0] + 1;
            start = mnv[0];
            end = mxval;
        }

        if (mnv[2] + 1 < a[mnv[1]].size())
        {
            mnheap.push({a[mnv[1]][mnv[2] + 1], mnv[1], mnv[2] + 1});
            mxval = max(mxval, a[mnv[1]][mnv[2] + 1]);
        }
        else
        {
            break;
        }
    }

    vector<int> res = {start, end};
    return res;
}

class Solution
{
public:
    vector<int> smallestRange(vector<vector<int>> &nums)
    {
        int k = nums.size();
        int n = nums[0].size();
        return answer(nums, k, n);
    }
};

int main()
{

    return 0;
}