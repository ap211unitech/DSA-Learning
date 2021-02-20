#include <bits/stdc++.h>
using namespace std;

void Insert(int arr[], int size)
{
    int index = size;
    int temp = arr[index];
    while (index > 1 && arr[index / 2] < temp)
    {
        arr[index] = arr[index / 2];
        index = index / 2;
    }
    arr[index] = temp;
}

int main()
{
    int arr[1999] = {0, 30, 50, 8, 16, 10, 15, 20};

    for (int i = 2; i < 8; i++)
        Insert(arr, i);

    arr[8] = 88;
    Insert(arr, 8);
    arr[9] = 19;
    Insert(arr, 9);
    arr[10] = 62;
    Insert(arr, 10);

    for (int i = 1; i < 11; i++)
        cout << arr[i] << " ";

    return 0;
}