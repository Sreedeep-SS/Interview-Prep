# data_structures.py

# =============================
# 1. LIST (Dynamic Array)
# =============================
def list_demo():
    arr = [1, 2, 3]
    arr.append(4)
    arr.insert(1, 10)
    arr.extend([7, 8])
    arr.pop()
    arr.remove(10)
    arr.sort()
    arr.reverse()
    return arr


# =============================
# 2. TUPLE (Immutable Sequence)
# =============================
def tuple_demo():
    tup = (1, 2, 3)
    return tup, tup[0], len(tup)


# =============================
# 3. SET (Unique Collection)
# =============================
def set_demo():
    s = {1, 2, 3}
    s2 = set([3, 4, 5])
    return {
        "union": s.union(s2),
        "intersection": s.intersection(s2),
        "difference": s.difference(s2),
    }


# =============================
# 4. DICTIONARY (HashMap)
# =============================
def dict_demo():
    d = {"a": 1, "b": 2}
    d["c"] = 3
    d.update({"d": 4})
    return d, list(d.keys()), list(d.values()), list(d.items())


# =============================
# 5. STACK (LIFO)
# =============================
from collections import deque

def stack_demo():
    stack = []
    stack.append(1)
    stack.append(2)
    top = stack.pop()
    return stack, top


def stack_demo_deque():
    stack = deque()
    stack.append(1)
    stack.append(2)
    top = stack.pop()
    return stack, top


# =============================
# 6. QUEUE (FIFO)
# =============================
def queue_demo():
    q = deque()
    q.append(1)
    q.append(2)
    first = q.popleft()
    return q, first


# =============================
# 7. HEAP (Priority Queue)
# =============================
import heapq

def heap_demo():
    pq = []
    heapq.heappush(pq, 3)
    heapq.heappush(pq, 1)
    heapq.heappush(pq, 2)
    smallest = heapq.heappop(pq)
    return pq, smallest


# =============================
# 8. LINKED LIST
# =============================
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def linked_list_demo():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    return head


# =============================
# 9. GRAPH (Adjacency List)
# =============================
def graph_demo():
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D"],
        "D": ["B", "C"],
    }
    graph["A"].append("D")
    return graph


# =============================
# 10. TREE (Binary Tree)
# =============================
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_demo():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    return root


# =============================
# MAIN TESTING AREA
# =============================
if __name__ == "__main__":
    print("List:", list_demo())
    print("Tuple:", tuple_demo())
    print("Set:", set_demo())
    print("Dict:", dict_demo())
    print("Stack:", stack_demo())
    print("Stack (Deque):", stack_demo_deque())
    print("Queue:", queue_demo())
    print("Heap:", heap_demo())
    print("Graph:", graph_demo())
    print("LinkedList Head Value:", linked_list_demo().val)
    print("Tree Root Value:", tree_demo().val)
