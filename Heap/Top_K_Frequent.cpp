#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pi;

int main()
{
    int n, k;
    cin >> n >> k;
    int arr[n];
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    unordered_map<int, int> freq;
    for (int i = 0; i < n; i++)
        freq[arr[i]]++;

    priority_queue<pi, vector<pi>, greater<pi>> minHeap;
    for (auto x : freq)
    {
        minHeap.push(make_pair(x.second, x.first));
        if (minHeap.size() > k)
        {
            minHeap.pop();
        }
    }

    for (int i = 0; i < k; i++)
    {
        pair<int, int> t = minHeap.top();
        cout << t.second << " ";
        minHeap.pop();
    }

    return 0;
}