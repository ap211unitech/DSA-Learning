#include <bits/stdc++.h>
using namespace std;

bool vis[100001];
int dist[100001];
vector<int> primes;
unordered_map<int, vector<int>> mp;

bool isPrime(int a)
{
    for (int i = 2; i * i <= a; i++)
    {
        if (a % i == 0)
        {
            return false;
        }
    }
    return true;
}

bool isDifferByOne(int a, int b)
{
    int cnt = 0;
    while (a > 0 and b > 0)
    {
        if (a % 10 != b % 10)
            cnt++;

        a = a / 10;
        b = b / 10;
    }
    if (cnt == 1)
    {
        return true;
    }
    return false;
}

void buildGraph(int a, int b)
{
    for (int i = 1000; i <= 9999; i++)
    {
        if (isPrime(i))
        {
            primes.push_back(i);
        }
    }

    for (int i = 0; i < primes.size(); i++)
    {
        for (int j = i + 1; j < primes.size(); j++)
        {
            int x, y;
            x = primes[i];
            y = primes[j];
            if (isDifferByOne(x, y))
            {
                mp[x].push_back(y);
                mp[y].push_back(x);
            }
        }
    }
}

void bfs(int src)
{

    queue<int> q;

    vis[src] = true;
    dist[src] = 0;
    q.push(src);

    while (q.size() > 0)
    {
        int curr = q.front();
        q.pop();

        for (int i : mp[curr])
        {
            if (vis[i] == false)
            {
                vis[i] = true;
                dist[i] = dist[curr] + 1;
                q.push(i);
            }
        }
    }
}

int main()
{

    int t;
    cin >> t;
    while (t--)
    {
        int a, b;
        cin >> a >> b;

        memset(vis, false, sizeof(vis));
        memset(dist, -1, sizeof(dist));
        primes.clear();
        mp.clear();

        buildGraph(a, b);

        bfs(a);

        if (dist[b] == -1)
        {
            cout << "Impossible" << endl;
        }
        else
        {
            cout << dist[b] << endl;
        }
    }

    return 0;
}