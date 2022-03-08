# 원형 이중 연결 리스트 구현하기

from __future__ import annotations
from typing import Any, Type

class Node:
    """원형 이중 연결 리스트용 노드 클래스"""

    def __init__(self, data: Any = None, prev: Node = None, next: Node = None) -> None:
        """초기화"""
        self.data = data
        self.prev = prev or self
        self.next = next or self

class DoubleLinkedList:
    """원형 이중 연결 리스트 클래스"""
    
    def __init__(self) -> None:
        """초기화"""
        self.head = self.current = Node()
        self.no = 0

    def __len__(self) -> bool:
        """연결 리스트의 노드 수를 반환"""
        return self.no

    def is_empty(self) -> bool:
        """리스트가 비었는지 확인"""
        return self.head.next is self.head

    def search(self, data: Any) -> Any:
        """data와 값이 같은 노드를 검색"""
        cnt = 0
        ptr = self.head.next
        while ptr is not self.head:
            if data == ptr.data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1

    def __contains__(self, data: Any) -> bool:
        """연결 리스트에 data가 포함되어 있는지 판단"""
        return self.search(data) >= 0

    
