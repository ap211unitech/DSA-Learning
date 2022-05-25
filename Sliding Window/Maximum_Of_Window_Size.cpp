
// Problem Link - https://practice.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1#

#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> arr = {1, 2, 3, 1, 4, 5, 2, 3, 6};
    int n = arr.size();
    int k = 3; // Window Size

    list<int> maxi;

    int i = 0;
    int j = 0;
    vector<int> res;

    while (j < n)
    {
        while (maxi.size() > 0 && maxi.back() < arr[j]) // Remove all elements smaller than arr[j]
        {
            maxi.pop_back();
        }
        maxi.push_back(arr[j]);

        if (j - i + 1 == k)
        {
            res.push_back(maxi.front());

            if (maxi.front() == arr[i])
            {
                maxi.pop_front();
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