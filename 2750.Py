from typing import Sequence, MutableSequence
from sys import stdin as s

def heapsort(a: MutableSequence) -> None:
    
    def heapify(a: MutableSequence, parent: int, last_idx: int):
        tmp = a[parent]
        
        # last_idx는 왼쪽 자식을 갖지 않는 첫번째 노드
        while parent < (last_idx + 1) // 2:
            left, right = parent * 2 + 1, parent * 2 + 2
            child = right if right <= last_idx and a[right] > a[left] else left
            if tmp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
            # parent = child
            
        a[parent] = tmp
        
        
    n = len(a)
    
    # (n-1)//2의 의미는 자식을 갖는 마지막 부모노드
    for i in range((n - 1) // 2, -1, -1):
        heapify(a, i, n - 1)
    
    for i in range(n - 1, 0, -1):
        #루트노드와 가장 마지막 노드의 값을 바꾼다.
        a[0], a[i] = a[i], a[0]
        #0 부터 i-1 인덱스까지 힙으로 만들기
        heapify(a, 0, i - 1)

if __name__=="__main__":
    s = open('input.txt', 'rt')
    n = int(s.readline())
    a = []
    for i in range(n):
        a.append(int(s.readline()))
    
    heapsort(a)
    for i in a:
        print(i)