#include <bits/stdc++.h>
using namespace std;

int partition(vector<int> &arr, int s, int e)
{
    int pivot = arr[s];
    int count = 0;
    // Count element less than pivot element
    for (int i = s + 1; i <= e; i++)
    {
        if (arr[i] <= pivot)
            count++;
    }

    // So, pivot index would be s+count
    int pivotIndex = s + count;

    // Swap correct pivotIndex position with original pivot
    swap(arr[pivotIndex], arr[s]);

    // Ensure that all elements on left side is lesser and right side elements are greater than pivotIndex value
    int i = s;
    int j = e;
    while (i < pivotIndex && j > pivotIndex)
    {
        while (arr[i] <= pivot)
        {
            i++;
        }

        while (arr[j] > pivot)
        {
            j--;
        }
        if (i < pivotIndex && j > pivotIndex)
        {
            swap(arr[i++], arr[j--]);
        }
    }

    return pivotIndex;
}

void quickSort(vector<int> &arr, int s, int e)
{
    if (s >= e)
        return;

    int pivotIndex = partition(arr, s, e);

    // Sort left and right part
    quickSort(arr, s, pivotIndex - 1);
    quickSort(arr, pivotIndex + 1, e);
}

int main()
{
    vector<int> arr = {24, 36, 21, 12, 8, 3, -1, -17, 1, 8, 36};
    int n = arr.size();

    quickSort(arr, 0, n - 1);

    for (auto i : arr)
        cout << i << " ";
    cout << endl;

    return 0;
}