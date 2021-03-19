#include <bits/stdc++.h>
using namespace std;

struct node
{
    int data;
    node *next;
};

void InsertAtEnd(struct node **l, int n)
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
        cout << l->data << " ";
        Display(l->next);
    }
}

bool ImproveMentSearch(struct node **l, int key)
{
    struct node *copy_of_l = *l;
    struct node *temp = NULL;
    while (copy_of_l != NULL)
    {
        if (copy_of_l->data == key)
        {
            temp->next = copy_of_l->next;
            copy_of_l->next = *l;
            *l = copy_of_l;
            return true;
        }
        temp = copy_of_l;
        copy_of_l = copy_of_l->next;
    }
    return false;
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
        InsertAtEnd(&l, k);
    }
    Display(l);
    cout << endl;

    if (ImproveMentSearch(&l, 6))
        cout << "Element Found" << endl;
    else
        cout << "Element Not Found" << endl;
    Display(l);
    cout << endl;
    return 0;
}