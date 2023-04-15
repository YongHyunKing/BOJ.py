import sys
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from queue import PriorityQueue
from functools import cmp_to_key
import collections
sys.setrecursionlimit(10**9)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while current:
            if val < current.val:
                if current.left is None:
                    current.left = new_node
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    break
                else:
                    current = current.right

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.val)
            self.inorder_traversal(node.right)
            
    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.val)

tree = BinaryTree()




if __name__ == "__main__":
    sys.stdin = open('input.txt', 'rt')
    while True:
        num = sys.stdin.readline()
        if num == '' : break
        tree.insert(int(num))
        
    tree.postorder_traversal(tree.root)
    

