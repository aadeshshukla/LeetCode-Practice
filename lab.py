win_positions = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
)

def game(player):
    print("\n", " | ".join(mesh[:3]))
    print("---+---+---")
    print("", " | ".join(mesh[3:6]))
    print("---+---+---")
    print("", " | ".join(mesh[6:]))

    while True:
        try:
            ch = int(input(f"Enter player {player}'s choice : "))
            if str(ch) not in mesh:
                raise ValueError
            mesh[ch-1] = player
            break
        except ValueError:
            print("Invalid position number.")

    for wp in win_positions:
        if all(mesh[pos] == player for pos in wp):
            return wp
    return None

player1 = "X"
player2 = "O"
player = player1
mesh = list("123456789")

for i in range(9):
    won = game(player)
    if won:
        print("\n", " | ".join(mesh[:3]))
        print("---+---+---")
        print("", " | ".join(mesh[3:6]))
        print("---+---+---")
        print("", " | ".join(mesh[6:]))
        print(f"*** Player {player} won! ***")
        break
    player = player1 if player == player2 else player2
else:
    print("Game ends in a draw.")

from collections import deque

def bfs(start_state):
    target = [1, 2, 3, 4, 5, 6, 7, 8 , 0]
    dq = deque([start_state])
    visited = {tuple(start_state): None}

    while dq:
        state = dq.popleft()
        if state == target:
            path = []
            while state:
                path.append(state)
                state = visited[tuple(state)]
            return path[::-1]

        zero = state.index(0)
        row, col = divmod(zero, 3)
        for move in (-3, 3, -1, 1):
            new_row, new_col = divmod(zero + move, 3)
            if 0 <= new_row < 3 and 0 <= new_col < 3 and abs(row - new_row) + abs(col - new_col) == 1:
                neighbor = state[:]
                neighbor[zero], neighbor[zero + move] = neighbor[zero + move], neighbor[zero]
                if tuple(neighbor) not in visited:
                    visited[tuple(neighbor)] = state
                    dq.append(neighbor)

def printSolution(path):
    for state in path:
        print("\n".join(' '.join(map(str, state[i:i+3])) for i in range(0, 9, 3)), end="\n-----\n")

startState = [1, 3, 0 , 6, 8, 4, 7, 5, 2]
solution = bfs(startState)
if solution:
    printSolution(solution)
    print(f"Solved in {len(solution) - 1} moves.")
else:
    print("No solution found.")






jug1, jug2, goal = 4, 3, 2
visited = [[False for _ in range(jug2 + 1)] for _ in range(jug1 + 1)]

def waterJug(vol1, vol2):
    if (vol1 == goal and vol2 == 0) or (vol2 == goal and vol1 == 0):
        print(vol1,"\t", vol2)
        print("Solution Found")
        return True

    if visited[vol1][vol2]:
        return False

    visited[vol1][vol2] = True
    print(vol1,"\t", vol2)

    return (
        waterJug(0, vol2) or 
        waterJug(vol1, 0) or 
        waterJug(jug1, vol2) or 
        waterJug(vol1, jug2) or 
        waterJug(vol1 + min(vol2, (jug1 - vol1)), vol2 - min(vol2, (jug1 - vol1))) or 
        waterJug(vol1 - min(vol1, (jug2 - vol2)), vol2 + min(vol1, (jug2 - vol2)))
    )

print("Steps: ")
print("Jug1 \t Jug2 ")
print("----- \t ------")
waterJug(0, 0)










from collections import deque

def tsp_bfs(graph):
    n = len(graph)
    startCity = 0
    min_cost = float('inf')
    opt_path = []
    dq = deque([([startCity], 0)])
    
    while dq:
        cur_path, cur_cost = dq.popleft()
        cur_city = cur_path[-1]
        
        if len(cur_path) == n:
            total_cost = cur_cost + graph[cur_city][startCity]
            if total_cost < min_cost:
                min_cost = total_cost
                opt_path = cur_path + [startCity]
            continue
        
        for next_city in range(n):
            if next_city not in cur_path:
                new_path = cur_path + [next_city]
                new_cost = cur_cost + graph[cur_city][next_city]
                dq.append((new_path, new_cost))
    
    return min_cost, opt_path

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

min_cost, opt_path = tsp_bfs(graph)
print(f"Minimum cost: {min_cost}")
print(f"Optimal path: {opt_path}")