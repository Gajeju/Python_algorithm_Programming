# 이진 검색 트리 구현하기

from __future__ import annotations
from typing import Any, Type

class Node:
    """이진 검색 트리의 노드"""
    def __init__(self, key: Any, value: Any, left: Node = None, right: Node = None):
        """생성자(constructor)"""
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    """이진 검색 트리"""

    def __init__(self):
        """초기화"""
        self.root = None
        
     