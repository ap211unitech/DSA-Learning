#include <bits/stdc++.h>
using namespace std;

struct Node
{
    int data;
    struct Node *lchild;
    struct Node *rchild;
    Node(int val)
    {
        data = val;
        lchild = NULL;
        rchild = NULL;
    }
};

void BuildTree(int pre[], int inorder[], int start, int end)
{
    if (start > end)
        return NULL;

    static int idx = 0;
    int curr = pre[idx];
    idx++;




}

int main()
{

    return 0;
}