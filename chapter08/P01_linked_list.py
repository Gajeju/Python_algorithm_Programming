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
            
    def remove(self, p: None) -> None:
        """노드 p를 삭제"""
        if self.head is not None:
            if p is self.head():
                self.remove_first()
            else:
                ptr = self.head
            while ptr.next is not p:
                ptr = ptr.next
                if ptr is None:
                    return
            ptr.next = p.next
            self.current = ptr
            self.no -= 1

        
    def remove_current_node(self) -> None:
        """주목 노드를 삭제"""
        self.remove(self.current)


    def clear(self) -> None:
        """전체 노드를 삭제"""
        while self.head is not None:
            self.remove_first()
        self.current = None
        self.no = 0

    
    def next(self) -> bool:
        """주목 노드를 한 칸 뒤로 이동"""
        if self.current is None or self.current.next is None:
            return False
        self.current = self.current.next
        return True


    def print_current_node(self) -> None:
        """주목 노드를 출력"""
        if self.current is None:
            print('주목 노드가 존재하지 않습니다.')
        else:
            print(self.current.data)
    

    def print(self) -> None:
        """모든 노드를 출력"""
        ptr = self.head

        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next

    
    def __iter__(self) -> LinkedListIterator:
        """이터레이터를 반환"""
        return LinkedListIterator(self.head)
    

class LinkedListIterator:
    """클래스 LinkedList의 이터레이터용 클래스"""

    def __init__(self, head: Node):
        self.current = head


    def __iter__(self) -> LinkedListIterator:
        return self
    

    def __next__(self) -> Any:
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data
    