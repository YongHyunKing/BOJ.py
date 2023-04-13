from sys import stdin as s
from typing import Sequence, MutableSequence
from queue import Queue
from collections import deque
from queue import PriorityQueue
import heapq
import sys

if __name__ == "__main__":
    s = open('input.txt', 'rt')
    n = int(s.readline())
    min_heap,max_heap = [],[]
    heapq.heappush(max_heap,-int(s.readline()))
    sys.stdout.write(str(-max_heap[0])+'\n')
    #max_heap이 하나 더 큰 것으로 
    for i in range(n-1):
        num = int(s.readline())
        if -max_heap[0]<num: heapq.heappush(min_heap,num)
        else : heapq.heappush(max_heap,-num)
        
        if len(max_heap)-len(min_heap)==2:
            heapq.heappush(min_heap,-heapq.heappop(max_heap))
        elif len(min_heap)-len(max_heap)==1:
            heapq.heappush(max_heap,-heapq.heappop(min_heap))
    
            
        sys.stdout.write(str(-max_heap[0])+'\n')