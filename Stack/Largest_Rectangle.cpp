#include <bits/stdc++.h>

using namespace std;

#define ll long long int

int main()
{
    ll n;
    cin >> n;
    ll arr[n];
    for (ll i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    // Next Smallest Left
    stack<ll> stack;
    vector<ll> NSL;
    ll i = 0;

    while (i < n)
    {
        while (!stack.empty() && arr[stack.top()] >= arr[i])
        {
            stack.pop();
        }
        if (!stack.empty())
            NSL.push_back(stack.top()); // Storing Index
        else
            NSL.push_back(-1);
        stack.push(i);
        i += 1;
    }

    while (!stack.empty())
    {
        stack.pop();
    }

    // Next Smallest right
    vector<ll> NSR;
    ll j = n - 1;

    while (j >= 0)
    {
        while (!stack.empty() && arr[stack.top()] >= arr[j])
        {
            stack.pop();
        }
        if (!stack.empty())
            NSR.push_back(stack.top()); // Storing Index
        else
            NSR.push_back(n);
        stack.push(j);
        j -= 1;
    }

    reverse(NSR.begin(), NSR.end());

    ll max_area = 0;

    for (ll i = 0; i < n; i++)
    {
        max_area = max(max_area, arr[i] * (NSR[i] - NSL[i] - 1));
    }

    cout << max_area;
    return 0;
}