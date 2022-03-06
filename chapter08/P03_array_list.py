# 커서로 연결 리스트 구현하기

from __future__ import annotations
from this import d
from typing import Any, Type

from numpy import inexact
from pymysql import NULL

Null = -1

class Node:
    """연결 리스트용 노드 클래스(배열 커서 버전)"""

    def __init__(self, data = Null, next = Null, dnext = Null):
        """초기화"""
        self.data = data
        self.next = next
        self.dnext = dnext

class ArrayLinkedList:
    """연결 리스트 클래스 (배열 커서 버전)"""

    def __init__(self, capacity: int):
        self.head = Null
        self.current = Null
        self.max = Null
        self.deleted = Null
        self.capacity = capacity
        self.n = [Node()] * self.capacity
        self.no = 0


    def __len__(self) -> int:
        """연결 리스트의 노드 수를 반환"""
        return self.no

    
    def get_insert_index(self):
        """다음에 삽입할 레코드의 인덱스를 구함"""
        if self.deleted == Null:
            if self.max + 1 < self.capacity:
                self.max += 1
                return self.max
            else:
                return Null
        else:
            rec = self.deleted
            self.deleted = self.n[rec].dnext
            return rec

    
    def delete_index(self, idx: int) -> None:
        """레코드 idx를 프리 리스트에 등록"""
        if self.deleted == Null:
            self.deleted = idx
            self.n[idx].dnext = NULL
        else:
            rec = self.deleted
            self.deleted = idx
            self.n[idx].dnext = rec

    
    def search(self, data: Any) -> int:
        """data와 값이 같은 노드를 탐색"""
        cnt = 0
        ptr = self.head
        while ptr != Null:
            if self.n[ptr].data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = self.n[ptr].next
        return Null

    
    def __contains__(self, data: Any) -> bool:
        """연결 리스트에 data가 포함되어 있는지 확인"""
        return self.search(data) >= 0


    def add_first(self, data: Any):
        """머리 노드에 삽입"""
        ptr = self.head
        rec = self.get_insert_index()
        if rec != Null:
            self.head = self.current = rec
            self.n[self.head] = Node(data, ptr)
            self.no += 1

    
    def add_last(self, data: Any) -> None:
        """꼬리 노드에 삽입"""
        pass