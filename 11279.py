from sys import stdin as s
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from queue import PriorityQueue


if __name__ == "__main__":
    s = open('input.txt', 'rt')
    que = PriorityQueue()
    n = int(s.readline())
    
    for i in range(n):
        num = int(s.readline())
        if num == 0:
            if que.empty(): print(0)
            else : print(-que.get())
        else : que.put(-num)
        
    

