// Leetcode - https://leetcode.com/problems/merge-k-sorted-lists/

#include <bits/stdc++.h>

using namespace std;

//  Definition for singly-linked list.
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

struct compare
{
    bool operator()(ListNode *a, ListNode *b)
    {
        return a->val > b->val;
    }
};

class Solution
{
public:
    ListNode *mergeKLists(vector<ListNode *> &arr)
    {
        int k = arr.size();

        priority_queue<ListNode *, vector<ListNode *>, compare> mnheap;

        for (int i = 0; i < k; i++)
        {
            if (arr[i])
                mnheap.push(arr[i]);
        }

        ListNode *res = NULL;
        ListNode *ptr = NULL;

        while (mnheap.size() > 0)
        {
            ListNode *mini = mnheap.top();
            mnheap.pop();

            if (res)
            {
                ptr->next = mini;
                ptr = ptr->next;
            }
            else
            {
                res = mini;
                ptr = mini;
            }

            if (mini && mini->next)
            {
                mnheap.push(mini->next);
            }
        }
        return res;
    }
};

int main()
{

    return 0;
}