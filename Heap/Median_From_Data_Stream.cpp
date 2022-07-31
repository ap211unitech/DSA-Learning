// Leetcode - https://leetcode.com/problems/find-median-from-data-stream/

#include <bits/stdc++.h>

using namespace std;

class MedianFinder
{
public:
    priority_queue<int> maxHeap;
    priority_queue<int, vector<int>, greater<int>> minHeap;

    MedianFinder()
    {
    }

    // Size of maxheap can be 1 large than minheap
    // i.e. sizeof(maxheap)-sizeof(minheap)<=1

    void addNum(int num)
    {

        int lsize = maxHeap.size();
        int rsize = minHeap.size();

        if (lsize == 0)
        {
            maxHeap.push(num);
        }
        else if (lsize == rsize)
        {
            if (num <= minHeap.top())
            {
                maxHeap.push(num);
            }
            else
            {
                int temp = minHeap.top();
                minHeap.pop();
                minHeap.push(num);
                maxHeap.push(temp);
            }
        }
        else if (lsize > rsize)
        {
            if (rsize == 0)
            {
                if (num >= maxHeap.top())
                {
                    minHeap.push(num);
                }
                else
                {
                    int temp = maxHeap.top();
                    maxHeap.pop();
                    maxHeap.push(num);
                    minHeap.push(temp);
                }
            }
            else if (num >= maxHeap.top())
            {
                minHeap.push(num);
            }
            else
            {
                int temp = maxHeap.top();
                maxHeap.pop();
                maxHeap.push(num);
                minHeap.push(temp);
            }
        }
    }

    double findMedian()
    {
        int lsize = maxHeap.size();
        int rsize = minHeap.size();
        double ans;

        if ((lsize + rsize) % 2 == 1)
        {
            ans = maxHeap.top();
        }
        else
        {
            ans = double(maxHeap.top() + minHeap.top()) / 2;
        }
        return ans;
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */

int main()
{

    return 0;
}