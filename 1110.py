from sys import stdin as s
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from queue import PriorityQueue
from functools import cmp_to_key

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n = int(s.readline())
    tmp = n
    cnt = 0
    while 1:
        cnt+=1
        if tmp<10: tmp = int(tmp*10+tmp)
        else:
            tmp2 = int(tmp//10) + int(tmp%10)
            tmp = int((tmp%10)*10)+int(tmp2%10)
        if tmp == n:
            break

    print(cnt)