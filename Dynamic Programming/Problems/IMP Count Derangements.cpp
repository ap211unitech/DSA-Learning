// Problem Link - https://www.codingninjas.com/codestudio/problems/count-derangements_873861?leftPanelTab=0&utm_source=youtube&utm_medium=affiliate&utm_campaign=Lovebabbar

// Approach is very good 

// Help Video - https://www.youtube.com/watch?v=NW-BLDQHFXk&list=PLDzeHZWIZsTomOPnCiU3J95WufjE36wsb&index=7

#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007

long long int countDerangements(int n)
{
    if (n == 1)
        return 0;
    if (n == 2)
        return 1;

    vector<long long int> dp(n + 1, -1);
    dp[1] = 0;
    dp[2] = 1;

    for (int i = 3; i <= n; i++)
    {
        dp[i] = (((i - 1) % MOD) * ((dp[i - 1] % MOD + dp[i - 2] % MOD) % MOD)) % MOD;
    }

    return dp[n];
}