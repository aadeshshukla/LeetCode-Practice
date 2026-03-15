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


def tower_of_hanoi(num, source, aux, target):
    if num == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(num - 1, source, target, aux)
    print(f"Move disk {num} from {source} to {target}")
    tower_of_hanoi(num - 1, aux, source, target)

num_disks = 3
tower_of_hanoi(num_disks, "A", "B", "C")



from collections import deque

def monkey_banana_problem():
    initial_state = ('Far-Chair', 'Chair-Not-Under-Banana', 'Off-Chair', 'Empty')
    goal_state = ('Near-Chair', 'Chair-Under-Banana', 'On-Chair', 'Holding')

    actions = {
        "Move to Chair": lambda state: ('Near-Chair', state[1], state[2], state[3]) if state[0] != 'Near-Chair' else None,
        "Push Chair under Banana": lambda state: ('Near-Chair', 'Chair-Under-Banana', state[2],  state[3]) if state[0] == 'Near-Chair' and state[1] != 'Chair-Under-Banana' else None,
        "Climb Chair": lambda state: ('Near-Chair', 'Chair-Under-Banana', 'On-Chair', state[3]) if state[0] == 'Near-Chair' and state[1] == 'Chair-Under-Banana' and state[2] != 'On-Chair' else None,
        "Grasp Banana": lambda state: ('Near-Chair', 'Chair-Under-Banana', 'On-Chair',  'Holding') if state[0] == 'Near-Chair' and state[1] == 'Chair-Under-Banana' and state[2] == 'On-Chair' and state[3] !='Holding' else None
    }

    dq = deque([(initial_state, [])])
    visited = set()

    while dq:
        current_state, actions_taken = dq.popleft()
        if current_state == goal_state:
            for action in actions_taken:
                print(action)
            return

        if current_state in visited:
            continue
        visited.add(current_state)

        for action_name, action_func in actions.items():
            next_state = action_func(current_state)
            if next_state and (next_state not in visited):
                dq.append((next_state, actions_taken + [f"Action: {action_name}"]))

monkey_banana_problem()









import math

def alpha_beta_pruning(depth, node_index, maximizing_player, values, alpha, beta):
    if depth == 0 or node_index >= len(values):
        return values[node_index]

    if maximizing_player:
        max_eval = -math.inf
        for i in range(2):
            eval = alpha_beta_pruning(depth - 1, node_index * 2 + i, False, values, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(2):
            eval = alpha_beta_pruning(depth - 1, node_index * 2 + i, True, values, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

values = [3, 5, 6, 9, 1, 2, 0, -1]
depth = 3
optimal_value = alpha_beta_pruning(depth, 0, True, values, -math.inf, math.inf)
print(f"The optimal value is: {optimal_value}")




def printSolution(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")

def isSafe(board, row, col, n):
    for i in range(row):
        if board[i][col]:
            return False
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j]:
            return False
        i -= 1
        j += 1
    return True

def solveNQueens(board, row, n):
    if row == n:
        printSolution(board)
        return True
    result = False
    for col in range(n):
        if isSafe(board, row, col, n):
            board[row][col] = 1
            result = solveNQueens(board, row + 1, n) or result
            board[row][col] = 0
    return result

def nQueens(n):
    board = [[0] * n for _ in range(n)]
    if not solveNQueens(board, 0, n):
        print("No solution exists.")

nQueens(8)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Sample dataset
data = {
    'Feature1': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'Feature2': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Class':    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

# Independent and dependent variables
X = df[['Feature1', 'Feature2']]
y = df['Class']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Logistic Regression
lr = LogisticRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)

# KNN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
knn_pred = knn.predict(X_test)

# Decision Tree
dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)
dt_pred = dt.predict(X_test)

# Accuracy scores
print("Logistic Regression Accuracy:", accuracy_score(y_test, lr_pred))
print("KNN Accuracy:", accuracy_score(y_test, knn_pred))
print("Decision Tree Accuracy:", accuracy_score(y_test, dt_pred))

# 
# 
# 
# 
