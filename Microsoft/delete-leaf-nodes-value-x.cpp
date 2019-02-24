#include <iostream>
#include <bits/stdc++.h>

using namespace std;

// A binary tree node
struct node {
  int data;
  struct node* left, *right;
};

// Allocate a new node
struct node* newNode(int data)
{
  struct node* newnode = new node;
  newnode->data = data;
  newnode->left = newnode->right = NULL;
  return (newnode);
}

// Delete leaves which have the value x
// Return root
node* deleteLeaves(node* root, int x)
{
  if (root==NULL)
    return NULL;
  root->left = deleteLeaves(root->left,x);
  root->right = deleteLeaves(root->right,x);

  if (root->data == x && root->left==NULL && root->right==NULL)
  {
    delete(root);
    return NULL;
  }
  return root;
}

// Print tree inorder
void inorder(node* root)
{
  if (root==NULL)
    return;
  inorder(root->left);
  cout << root->data << " ";
  inorder(root->right);
}

// Driver program
int main()
{
  struct node* root = newNode(6);
  root->left = newNode(5);
  root->right = newNode(4);
  root->left->left = newNode(1);
  root->left->right = newNode(2);
  root->right->right = newNode(5);

  deleteLeaves(root,5);

  inorder(root);
  cout << "\n";

  return 0;
}
