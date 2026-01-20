#BREADTH FIRST SEARCH ALGORITHM
# graph={
#     'A': ['B', 'C'],    
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }
# visitedNodes=[]
# queueNodes=[]
# def bfs(visitedNodes, graph, node):
#     visitedNodes.append(node)
#     queueNodes.append(node)

#     while queueNodes:
#         m = queueNodes.pop(0)
#         print(m, end=" ")

#         for neighbor in graph[m]:
#             if neighbor not in visitedNodes:
#                 visitedNodes.append(neighbor)
#                 queueNodes.append(neighbor)
# snode=input("Enter the starting node: ").upper()
# bfs(visitedNodes, graph,snode)
# ___________________________________
# BINARY SEARCH ALGORITHM
lst=[1,2,3,4,5]
target=5
def search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
result = search(lst, target)
print(f"Target {target} found at index: {result}")

