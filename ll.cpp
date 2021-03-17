#include <bits/stdc++.h>
using namespace std;

struct node
{
    int data;
    node *next;
};

void Insert(struct node **l, int n)
{
    struct node *newNode = new node;
    newNode->data = n;
    newNode->next = NULL;
    if (*l == NULL)
        *l = newNode;
    else
    {
        struct node *temp = *l;
        while (temp->next != NULL)
        {
            temp = temp->next;
        }
        temp->next = newNode;
    }
}

void Display(struct node *l)
{
    // while (l != NULL)
    // {
    //     cout << l->data << " ";
    //     l = l->next;
    // }
    if (l != NULL)
    {
        Display(l->next);
        cout << l->data << " ";
    }
}

int main()
{
    int n;
    cin >> n;
    struct node *l = NULL;
    while (n--)
    {
        int k;
        cin >> k;
        Insert(&l, k);
    }
    Display(l);
    return 0;
}