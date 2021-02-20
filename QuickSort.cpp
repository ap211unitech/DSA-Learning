#include <bits/stdc++.h>
using namespace std;

int Partition(int arr[], int l, int h)
{
    int pivot = arr[l];
    int i = l, j = h;
    while (i < j)
    {
        do
        {
            i++;
        } while (arr[i] <= pivot);
        do
        {
            j--;
        } while (arr[j] > pivot);
        if (i < j)
        {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    int temp = arr[l];
    arr[l] = arr[j];
    arr[j] = temp;
    return j;
}

void QuickSort(int arr[], int l, int h)
{
    if (l < h)
    {
        int j = Partition(arr, l, h);
        QuickSort(arr, l, j);
        QuickSort(arr, j + 1, h);
    }
}

int main()
{
    int n = 9;
    int arr[] = {10, 3, 16, 32, 78, 41, 1, 90, 26};
    QuickSort(arr, 0, n);
    for (int i = 0; i < 9; i++)
        cout << arr[i] << " ";
    return 0;
}