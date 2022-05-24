#include <bits/stdc++.h>
using namespace std;


int main()
{
    int n, k, x;
    cin >> n >> k >> x;
    int arr[n];
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    priority_queue<pair<int, int>> maxHeap;
    int diff[n];

    for (int i = 0; i < n; i++)
        diff[i] = abs(arr[i] - x);

    for (int i = 0; i < n; i++)
    {
        maxHeap.push(make_pair(diff[i], arr[i]));
        if (maxHeap.size() > k)
            maxHeap.pop();
    }

    while (maxHeap.size())
    {
        pair<int, int> top = maxHeap.top();
        cout << top.second << " ";
        maxHeap.pop();
    }

    return 0;
}