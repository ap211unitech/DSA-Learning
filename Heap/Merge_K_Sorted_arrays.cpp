// Interview Bit - https://www.interviewbit.com/problems/merge-k-sorted-arrays/

#include <bits/stdc++.h>

using namespace std;
struct compare
{
    bool operator()(vector<int> &a, vector<int> &b)
    {
        return a[0] > b[0];
    }
};

vector<int> solve(vector<vector<int>> &arr)
{
    int k = arr.size();
    int n = arr[0].size();

    priority_queue<vector<int>, vector<vector<int>>, compare> mnheap;

    for (int i = 0; i < k; i++)
    {
        mnheap.push({arr[i][0], i, 0});
    }

    vector<int> res;

    while (mnheap.size() > 0)
    {
        vector<int> mini = mnheap.top();

        int val = mini[0];
        int i = mini[1];
        int j = mini[2];
        mnheap.pop();

        res.push_back(val);

        if (j + 1 < n)
        {
            mnheap.push({arr[i][j + 1], i, j + 1});
        }
    }
    return res;
}

int main()
{

    return 0;
}