
// Problem Link - https://practice.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1

#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> arr = {-8, 2, 3, -6, 10};
    int n = arr.size();
    int k = 2; // Window Size

    queue<int> negatives;

    long long int i = 0;
    long long int j = 0;

    vector<long long int> res;

    while (j < n)
    {
        if (arr[j] < 0)
        {
            negatives.push(arr[j]);
        }

        if (j - i + 1 == k) // Window size == k
        {
            if (negatives.size() == 0) // Means no negative values in that window
            {
                res.push_back(0);
            }
            else
            {
                int firstNeg = negatives.front();
                res.push_back(firstNeg);
            }

            if (arr[i] == negatives.front() && negatives.size() > 0) // index of i is negative, needed to remove
            {
                negatives.pop();
            }
            i++;
        }

        j++;
    }

    for (auto i : res)
        cout << i << " ";
    cout << endl;

    return 0;
}