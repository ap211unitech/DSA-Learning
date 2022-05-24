#include <bits/stdc++.h>
using namespace std;

void merge(vector<int> &arr, int s, int e)
{
    // arr is sorted in two parts -
    // 1) from index s to mid
    // 2) from index mid+1 to e

    int mid = s + (e - s) / 2;

    vector<int> left;
    int leftSize = mid - s + 1;
    int index = s;
    for (int i = 0; i < leftSize; i++)
        left.push_back(arr[index++]);

    vector<int> right;
    int rightSize = e - mid;
    index = mid + 1;
    for (int i = 0; i < rightSize; i++)
        right.push_back(arr[index++]);

    index = s;
    int i = 0;
    int j = 0;

    while (i < left.size() && j < right.size())
    {
        if (left[i] > right[j])
        {
            arr[index++] = right[j++];
        }
        else
        {
            arr[index++] = left[i++];
        }
    }

    while (i < left.size())
    {
        arr[index++] = left[i++];
    }

    while (j < right.size())
    {
        arr[index++] = right[j++];
    }
}

void mergeSort(vector<int> &arr, int s, int e)
{
    if (s >= e)
        return;

    int mid = s + (e - s) / 2;

    // Left part sorting
    mergeSort(arr, s, mid);
    // Right part sorting
    mergeSort(arr, mid + 1, e);

    // Merging both parts
    merge(arr, s, e);
}

int main()
{
    vector<int> arr = {23, 12, 3, 7, 35};
    int n = arr.size();

    mergeSort(arr, 0, n - 1);

    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;

    return 0;
}