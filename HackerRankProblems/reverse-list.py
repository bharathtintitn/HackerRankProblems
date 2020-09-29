from __future__ import print_function
import pdb

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self, head):
    temp = head
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def reverse(head):
  curr = head.next
  prev = None
  while curr:
      temp = curr.next
      curr.next = head
      head.next = prev
      prev = head
      head = curr
      curr = temp
  return head


def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)
  head.print_list(head)
  head = reverse(head)
  head.print_list(head)

main()
