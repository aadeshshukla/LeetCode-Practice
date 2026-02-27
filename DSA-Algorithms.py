# dsa ALgorithms 
# 1. Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
# 2. Merge Sort 
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)
def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# 3. Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 4. Dijkstra's Algorithm
import heapq
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

# 5. A* Search Algorithm
def a_star_search(graph, start, goal, heuristic):
    open_set = [(0 + heuristic[start], start)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            return reconstruct_path(came_from, current)
        for neighbor, weight in graph[current].items():
            tentative_g_score = g_score[current] + weight
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic[neighbor]
                heapq.heappush(open_set, (f_score, neighbor))
    return None
def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]

# 6. Dynamic Programming
def fibonacci(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# 7. Backtracking
def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
                return False
        return True
    def solve(row):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(row + 1)
    result = []
    board = [-1] * n
    solve(0)
    return result
# 8. Depth-First Search (DFS)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)  # Process the node (e.g., print it)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# 9. Breadth-First Search (BFS)
from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        current = queue.popleft()
        print(current)  # Process the node (e.g., print it)
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# 10. Knapsack Problem
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]

# 11. Floyd-Warshall Algorithm
def floyd_warshall(graph):
    dist = {node: {neighbor: float('inf') for neighbor in graph} for node in graph}
    for node in graph:
        dist[node][node] = 0
        for neighbor, weight in graph[node].items():
            dist[node][neighbor] = weight
    for k in graph:
        for i in graph:
            for j in graph:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
# 12. Bellman-Ford Algorithm
def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
    # Check for negative-weight cycles
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Graph contains a negative-weight cycle")
    return distances
# 13. Topological Sort
def topological_sort(graph):
    visited = set()
    stack = []
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)
    for node in graph:
        if node not in visited:
            dfs(node)
    return stack[::-1]
# 14. Union-Find (Disjoint Set Union)
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

# 15. Reverse Nodes in k-Group (Linked List)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_k_group(head, k):
    def get_length(node):
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    def reverse_group(start, end):
        prev = None
        current = start
        while current != end:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    length = get_length(head)
    if length < k:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev_group_end = dummy

    while length >= k:
        group_start = prev_group_end.next
        group_end = group_start
        for _ in range(k - 1):
            group_end = group_end.next

        next_group_start = group_end.next

        reversed_group_head = reverse_group(group_start, next_group_start)

        prev_group_end.next = reversed_group_head
        group_start.next = next_group_start

        prev_group_end = group_start
        length -= k

    return dummy.next

# Example usage:
# Create a linked list 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
k = 2
new_head = reverse_k_group(head, k)
# Print the reversed linked list
current = new_head
while current:
    print(current.val, end=' ')
    current = current.next
# Output: 2 1 4 3 5

# lets take linked list and k dynamically
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=' ')
        current = current.next
    print()
# Example usage:
arr = [1, 2, 3, 4, 5]
k = 3
head = create_linked_list(arr)
new_head = reverse_k_group(head, k)
print_linked_list(new_head)
# Output: 3 2 1 4 5

# 16. Longest Common Subsequence (LCS)
def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

# 17. Longest Increasing Subsequence (LIS)
def longest_increasing_subsequence(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
