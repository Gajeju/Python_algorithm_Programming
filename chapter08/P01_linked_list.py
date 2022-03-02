# 포인터로 연결 리스트 구현하기

from __future__ import annotations
from typing import Any, Type

class Node:
    """연결 리스트용 노드 클래스"""

    def __init__(self, data: Any = None, next: Node = None):
        """초기화"""
        self.data = data
        self.next = next


class LinkedList:
    """연결 리스트 클래스"""

    def __init__(self) -> None:
        """초기화"""
        self.no = 0
        self.head = None
        self.current = None
    

    def __len__(self) -> int:
        """연결 리스트의 노드 개수를 반환"""
        return self.no
    

    def search(self, data: Any) -> int:
        """data와 값이 같은 노드를 검색"""
        cnt = 0
        ptr = self.head
        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1


    def __contains__(self, data: Any) -> bool:
        """연결 리스트에 data가 포함되어 있는지 확인"""
        return self.search(data) >= 0


    def add_first(self, data: Any) -> None:
        """맨 앞에 노드를 삽입"""
        ptr = self.head
        self.head = self.current = Node(data, ptr)
        self.no += 1


    def add_last(self, data: Any):
        """맨 끝에 노드를 삽입"""
        if self.head is None:
            self.add_first(data)
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = self.current = Node(data, None)
            self.no += 1

    
    def remove_first(self) -> None:
        """머리 노드를 삭제"""
        if self.head is not None:
            self.head = self.current = self.head.next
        self.no -= 1
    

    def remove_last(self):
        """꼬리 노드를 삭제"""
        if self.head is not None:
            if self.head.next is None:
                self.remove_first()
            else:
                ptr = self.head
                pre = self.head
            while ptr.next is not None:
                pre = ptr
                ptr = ptr.next 
            pre.next = None
            self.current = pre
            self.no -= 1
            