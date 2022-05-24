#include <bits/stdc++.h>

using namespace std;

struct Node
{
    int data;
    struct Node *left;
    struct Node *right;
};

struct Node *createNode(int data)
{
    struct Node *newNode = new struct Node;
    newNode->data = data;
    newNode->left = newNode->right = NULL;
    return newNode;
}

void Inorder(struct Node *root)
{
    if (root == NULL)
    {
        return;
    }
    Inorder(root->left);
    cout << root->data << " ";
    Inorder(root->right);
}

int main()
{

    struct Node *root = createNode(3);
    root->left = createNode(9);
    root->right = createNode(7);
    Inorder(root);
    return 0;
}