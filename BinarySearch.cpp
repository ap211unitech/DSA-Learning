#include <bits/stdc++.h>
using namespace std;

void Search(int arr[], int low, int high, int key)
{
    if (low <= high)
    {
        int mid = (low + high) / 2;
        if (arr[mid - 1] == key)
            cout << "Element is found at index " << mid << endl;
        else if (arr[mid - 1] < key)
            Search(arr, mid + 1, high, key);
        else
            Search(arr, low, mid - 1, key);
    }
    else
        cout << "Not found\n";
}

int main()
{
    int arr[] = {8, 12, 34, 56, 78, 90, 123};
    Search(arr, 1, 7, 8);
    return 0;
}