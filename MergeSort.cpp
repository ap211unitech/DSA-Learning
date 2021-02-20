#include <bits/stdc++.h>
using namespace std;

void Merge(int arr[], int l, int mid, int h)
{
    int i = l, j = mid + 1, k = l;
    int B[100];

    while (i <= mid && j <= h)
    {
        if (arr[i] < arr[j])
            B[k++] = arr[i++];
        else
            B[k++] = arr[j++];
    }
    for (; i <= mid; i++)
        B[k++] = arr[i];
    for (; j <= h; j++)
        B[k++] = arr[j];

    for (i = l; i <= h; i++)
        arr[i] = B[i];
}

void IMergeSortAlgorithm(int arr[], int n)
{
    int p, l, h, mid, i;

    for (p = 2; p <= n; p = p * 2)
    {
        for (i = 0; i + p - 1 <= n; i = i + p)
        {
            l = i;
            h = i + p - 1;
            mid = (l + h) / 2;
            Merge(arr, l, mid, h);
        }
    }
    if (p / 2 < n)
        Merge(arr, 0, (p / 2) - 1, n);
}

void RMergeSortAlgorithm(int arr[], int l, int h)
{
    int mid;
    if (l < h)
    {
        mid = (l + h) / 2;
        RMergeSortAlgorithm(arr, l, mid);
        RMergeSortAlgorithm(arr, mid + 1, h);
        Merge(arr, l, mid, h);
    }
}

int main()
{
    int n = 9;
    int arr[] = {10, 3, 16, 32, 78, 41, 1, 90, 26};
    // IMergeSortAlgorithm(arr, n);
    RMergeSortAlgorithm(arr, 0, n - 1);
    for (int i = 0; i < 9; i++)
        cout << arr[i] << " ";
    return 0;
}