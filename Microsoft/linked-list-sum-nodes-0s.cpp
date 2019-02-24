/*
 * Problem link: https://www.geeksforgeeks.org/linked-list-sum-nodes-0s/
 */

#include <iostream>
#include <stdlib.h>
#define NODE struct node

NODE
{
  int data;
  struct node *next;
};

NODE *getNode(int val)
{
  NODE *tmp;
  tmp = (NODE*)malloc(sizeof(NODE));
  tmp->data = val;
  tmp->next = NULL;
  return tmp;
}

void printList(NODE *head)
{
  while (head->next != NULL)
  {
    printf("%d->",head->data);
    head = head->next;
  }
  printf("%d\n",head->data);
}

void inPlaceStore(NODE *head)
{
  if (head->data==0)
  {
    head=head->next;
  }
  // modified list
  NODE *modified = head;

  NODE *temp = head;
  int sum=0;

  while (temp)
  {
    //printf("%d\n",head->data);
    if(temp->data != 0)
    {
      sum+= temp->data;
      temp = temp->next;
    }

    else
    {
      //printf("%d\n",head->data);
      modified->data=sum;
      modified->next=temp->next;
      temp=temp->next;
      modified=temp;
      sum=0;
    }
    printList(head);
  }
  printList(head);
}

int main()
{
  NODE *head;
  head = getNode(3);
  head->next = getNode(2);
  head->next->next = getNode(0);
  head->next->next->next = getNode(4);
  head->next->next->next->next = getNode(5);
  head->next->next->next->next->next = getNode(0);
  head->next->next->next->next->next->next = getNode(6);
  head->next->next->next->next->next->next->next = getNode(7);
  inPlaceStore(head);
  return 0;
}
