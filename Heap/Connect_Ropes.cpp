#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long int n;
    cin >> n;
    long long int arr[n];
    for (long long int i = 0; i < n; i++)
        cin >> arr[i];

    priority_queue<long long int, vector<long long int>, greater<long long int>> minHeap;
    for (long long int i = 0; i < n; i++)
        minHeap.push(arr[i]);

    long long int cost = 0;
    while (minHeap.size() >= 2)
    {
        long long int top1 = minHeap.top();
        minHeap.pop();
        long long int top2 = minHeap.top();
        minHeap.pop();
        cost += top1 + top2;
        minHeap.push(top1 + top2);
    }

    cout << cost << endl;

    return 0;
}