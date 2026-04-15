from collections import deque

def bfs_traversal(graph, start, goal):
    queue = deque()
    visited = set()
    result = []
    parent = {}

    queue.append(start)
    visited.add(start)
    parent[start] = None



    while queue:

        node = queue.popleft()
        result.append(node)

        if node == goal:
            break

        for neigh in graph.get(node , []):
            if neigh not in visited:
                visited.add(neigh)
                queue.append(neigh)
                parent[neigh] = node

    #Path reconstructing

    path = []
    curr = goal

    while curr is not None:
        path.append(curr)
        curr = parent[curr]

    path.reverse()

    return result, path



n = int(input("Enter the Number of Nodes:- "))
print("Enter the Node labels:- ")
labels = input().split()

graph = {node : [] for node in labels}

m = int(input("No of Edges:- "))

print("Enter the Edge in (u,v) Formate:- ")

for _ in range(m):
    u , v = input().split()
    graph[u].append(v)
start = input("Enter the start Node:- ")
goal = input("Enter the goal Node:- ")
res, path = bfs_traversal(graph, start, goal)
print("BFS Traversal:- ", res)
print("Shortest Path:", " -> ".join(path))




def dfs(graph, start, goal):
    stack = []
    visited = set()
    dfs_order = []
    parent = {}

    stack.append(start)
    visited.add(start)
    dfs_order.append(start)
    parent[start] = None

    print(f"Pushed {start} -> Stack {stack}")

    while stack:
        node = stack[-1]

        pushed = False

        if node == goal:
            break

        for neigh in graph.get(node, []):
            if neigh not in visited:
                dfs_order.append(neigh)
                visited.add(neigh)
                stack.append(neigh)
                parent[neigh] = node
                print(f"Pushed {neigh} -> Stack {stack}")
                pushed = True
                break

        if not pushed:
            popped = stack.pop()
            print(f"Popped {popped} -> Stack {stack}")

    #Path Reconstruction
    path = []
    curr =goal

    while curr is not None:
        path.append(curr)
        curr =parent[curr]

    path.reverse()

    return dfs_order, path


n = int(input("Enter the Number of Nodes: "))
print("Enter the Labels:- ")
labels = input().split()

graph = {node : [] for node in labels}

m = int(input("Enter the no:of edges:- "))
print("Enter the Edges in u, v formate:- ")

for _ in range(m):
    u , v = input().split()
    graph[u].append(v)

start = input("Enter the Start Node:")
goal = input("Enter the End Node:")
res, path = dfs(graph , start, goal)
print("DFS Traversal:- ", res)
print("Path Found:- ","->".join(path))



from heapq import heappush, heappop
def ucs(graph, start, goal):

    pq = [(0, start)]
    visited=set()
    parent={start:None}

    while pq:
        cost, node = heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            path = []
            curr = goal

            while curr:
                path.append(curr)
                curr = parent[curr]

            path.reverse()
            print("Path :- ", "->".join(path))
            print("Cost :- ", cost)

            return

        for neigh, w in graph[node]:
            if neigh not in visited:
                heappush(pq,(cost + w, neigh))
                parent[neigh] = node

# graph = {
#     'A': [('B', 1), ('C', 4)],
#     'B': [('D', 2)],
#     'C': [('D', 1)],
#     'D': []
# }
#
# ucs(graph, 'A', 'D')

n = int(input("Enter the number of nodes:- "))
print("Enter the Node labels:- ")
labels = input().split()

graph = {node : [] for node in labels}

m = int(input("Enter the Number of edges:- "))
print("Enter the cost and weight in u,v,c Formate:- ")
for _ in range(m):
    u, v, c = input().split()
    graph[u].append((v, int(c)))
start = input("Enter the start Node:- ")
end = input("Enter the End Node:- ")

ucs(graph, start, end)


from heapq import heappush, heappop

def greedy(graph, h, start, goal):
    pq = [(h[start],start)]
    visited = set()
    parent={start:None}

    while pq:
        _, node = heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            path = []
            cur = goal

            while cur:
                path.append(cur)
                cur = parent[cur]
            path.reverse()
            print("Path:", " -> ".join(path))
            return

        for neigh, _ in graph[node]:
            if neigh not in visited:
                parent[neigh] = node
                heappush(pq, (h[neigh],neigh))

# graph = {
#     'A': [('B',1), ('C',4)],
#     'B': [('D',2)],
#     'C': [('D',1)],
#     'D': []
# }

# h = {
#     'A': 3,
#     'B': 2,
#     'C': 1,
#     'D': 0
# }

# greedy(graph, h, 'A', 'D')
print("---- GREEDY BEST FIRST SEARCH ----\n")

n = int(input("Enter number of nodes: "))
labels = input("Enter node labels: ").split()

graph = {node: [] for node in labels}
heuristic = {}

print("Enter heuristic value for each node:")
for node in labels:
    heuristic[node] = int(input(f"h({node}) = "))

m = int(input("Enter number of edges: "))
print("Enter edges (u v cost):")
for _ in range(m):
    u, v, c = input().split()
    graph[u].append((v, int(c)))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

path = greedy(graph, heuristic, start, goal)

from heapq import heappush, heappop


def astar(graph, h, start, goal):
    pq = [(h[start], 0, start)]  # (f, cost, node)
    visited = set()
    parent = {start: None}

    while pq:
        f, cost, node = heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            # build path
            path = []
            cur = goal
            while cur:
                path.append(cur)
                cur = parent[cur]
            path.reverse()

            print("Path:", " -> ".join(path))
            print("Cost:", cost)
            return

        for neigh, w in graph[node]:
            if neigh not in visited:
                parent[neigh] = node
                new_cost = cost + w
                heappush(pq, (new_cost + h[neigh], new_cost, neigh))





def cost(tour, dist):
    cost = 0

    for i in range(len(tour) - 1):
        cost+=dist[tour[i]][tour[i + 1]]
    cost+=dist[tour[0]][tour[-1]]
    return cost

def tsp(dist):

    n = len(dist)
    tour = list(range(n))

    best_cost = cost(tour, dist)

    while True:
        improved = False

        for i in range(1, n+1):
            for j in range(i, n):
                new_tour = tour[:]

                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]

                new_cost = cost(new_tour, dist)

                if new_cost < best_cost:
                    best_cost = new_cost
                    tour = new_tour
                    improved = True

        if not improved:
            break
    return tour, best_cost


n = int(input("Enter the number of nodes: "))
dist = []

for _ in range(n):
    dist.append(list(map(int, input().split())))

tour, cost = tsp(dist)

print("Tour:", tour)
print("Cost:", cost)



from heapq import heappop, heappush

def waterjug(capA, capB, target):
    pq = [(0,0,(0,0),[])]
    visited = set()

    while pq:

        f, steps, (a,b) , path = heappop(pq)

        if a == target or b == target:
            path.append(("Goal Reached", (a,b)))
            return path

        if (a,b) in visited:
            continue
        visited.add((a,b))

        actions = [
            ("Fill A", (capA, b)),
            ("Fill B", (a, capB)),
            ("Empty A", (0, b)),
            ("Empty B", (a, 0)),
            ("Pour A→B", (a - min(a, capB - b), b + min(a, capB - b))),
            ("Pour B→A", (a + min(b, capA - a), b - min(b, capA - a)))
        ]

        for act, (na,nb) in actions:
            if (na, nb) not in visited:
                h = min(abs(na - target), abs(nb - target))
                heappush(pq, (steps + 1 + h, steps+1, (na, nb),path+[(act, (a,b))]))

    return None


# 🔹 INPUT
capA = int(input("Enter capacity of Jug A: "))
capB = int(input("Enter capacity of Jug B: "))
target = int(input("Enter target: "))

# 🔹 CALL FUNCTION
result = waterjug(capA, capB, target)

# 🔹 OUTPUT
if result:
    for i, (act, (a, b)) in enumerate(result):
        print(f"Step {i}: {act}")
        print(f"A = {a}, B = {b}")
else:
    print("No solution")


# N Queens
def safe(board, row, col):
    # check column
    for i in range(row):
        if board[i] == col:
            return False

    # check left diagonal
    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    # check right diagonal
    i, j = row-1, col+1
    while i >= 0 and j < len(board):
        if board[i] == j:
            return False
        i -= 1
        j += 1

    return True

def print_board(board):
    n = len(board)

    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print('Q',end=" ")
            else:
                print('*',end=" ")
        print()
    print()


def solve(board, row, n):
    if row == n:
        print_board(board)   # print solution
        return

    for col in range(n):
        if safe(board, row, col):
            board[row] = col
            solve(board, row+1, n)
            board[row] = -1   # backtrack


# INPUT
n = int(input("Enter N: "))
board = [-1] * n

# CALL
solve(board, 0, n)

# WUMPPUS
from collections import deque

def bfs(start, goal, size, pits, wumpus):
    queue = deque()
    visited = set()

    queue.append((start, [start]))
    visited.add(start)

    while queue:
        node, path = queue.popleft()

        if node == goal:
            return path

        r, c = node

        # 4 directions
        neighbors = [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]

        for nr, nc in neighbors:
            if 1 <= nr <= size and 1 <= nc <= size:
                if (nr, nc) not in visited and (nr, nc) not in pits and (nr, nc) != wumpus:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), path + [(nr, nc)]))

    return None


# INPUT
size = int(input("Enter grid size: "))
pits = []

n = int(input("Enter number of pits: "))
for _ in range(n):
    pits.append(tuple(map(int, input().split())))

wumpus = tuple(map(int, input("Enter Wumpus location: ").split()))
goal = tuple(map(int, input("Enter Gold location: ").split()))

start = (1, 1)

# OUTPUT
path = bfs(start, goal, size, pits, wumpus)

if path:
    print("Path:", path)
else:
    print("No path")


#FOL
facts = []
rules = []


def add_fact():
    f = input("Enter fact: ")
    facts.append(f)


def add_rule():
    r = input("Enter rule (A(x)->B(x)): ")
    rules.append(r)


def query():
    q = input("Enter query: ")

    if q in facts:
        print("TRUE (Fact)")
        return

    for r in rules:
        left, right = r.split("->")

        if q.split("(")[0] in right:
            val = q[q.find("(") + 1:q.find(")")]
            if left.replace("x", val) in facts:
                print("TRUE (Derived)")
                return

    print("FALSE")


while True:
    print("\n1.Add Fact\n2.Add Rule\n3.Query\n4.Exit")
    ch = input("Choice: ")

    if ch == '1':
        add_fact()
    elif ch == '2':
        add_rule()
    elif ch == '3':
        query()
    else:
        break

#TIC TAC TOE
import math

board = [' '] * 9


def print_board():
    for i in range(0, 9, 3):
        print(board[i:i + 3])


def check(p):
    win = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
           (0, 3, 6), (1, 4, 7), (2, 5, 8),
           (0, 4, 8), (2, 4, 6)]
    return any(board[a] == board[b] == board[c] == p for a, b, c in win)


def moves_left():
    return ' ' in board


def minimax(is_max):
    if check('O'): return 1
    if check('X'): return -1
    if not moves_left(): return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = max(best, minimax(False))
                board[i] = ' '
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = min(best, minimax(True))
                board[i] = ' '
        return best


def best_move():
    best_val = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            val = minimax(False)
            board[i] = ' '
            if val > best_val:
                best_val = val
                move = i
    return move


while True:
    print_board()
    pos = int(input("Enter position (1-9): ")) - 1

    if pos < 0 or pos > 8 or board[pos] != ' ':
        print("Invalid move")
        continue

    board[pos] = 'X'

    if check('X'):
        print_board()
        print("You win")
        break

    if not moves_left():
        print("Draw")
        break

    board[best_move()] = 'O'

    if check('O'):
        print_board()
        print("AI wins")
        break

#BAYES
from itertools import product


# ----------- NODE STRUCTURE -----------

class Node:
    def __init__(self, name, values, parents):
        self.name = name
        self.values = values
        self.parents = parents
        self.cpt = {}  # {(parent_vals): {value: prob}}

    def get_prob(self, value, assignment):
        if not self.parents:
            return self.cpt[()][value]

        key = tuple(assignment[p] for p in self.parents)
        return self.cpt[key][value]

    # ----------- ENUMERATION -----------


def enumerate_all(vars_list, evidence, bn):
    if not vars_list:
        return 1.0

    Y = vars_list[0]
    node = bn[Y]

    if Y in evidence:
        prob = node.get_prob(evidence[Y], evidence)
        return prob * enumerate_all(vars_list[1:], evidence, bn)

    total = 0
    for y in node.values:
        new_evidence = evidence.copy()
        new_evidence[Y] = y
        prob = node.get_prob(y, new_evidence)
        total += prob * enumerate_all(vars_list[1:], new_evidence, bn)

    return total


# ----------- QUERY FUNCTION -----------

def query(var, evidence, bn, order):
    Q = {}

    for val in bn[var].values:
        e = evidence.copy()
        e[var] = val
        Q[val] = enumerate_all(order, e, bn)

        # Normalize
    total = sum(Q.values())
    for k in Q:
        Q[k] /= total

    return Q


# ----------- INPUT -----------

def build_network():
    n = int(input("Enter number of variables: "))
    bn = {}
    order = []

    for _ in range(n):
        name = input("\nVariable name: ")
        order.append(name)

        values = input(f"Values of {name} (space-separated): ").split()
        parents = input(f"Parents of {name} (or 'none'): ").split()

        if parents == ['none']:
            parents = []

        node = Node(name, values, parents)

        print(f"Enter CPT for {name}:")

        if not parents:
            probs = input(f"Enter probabilities for {values}: ").split()
            node.cpt[()] = {v: float(p) for v, p in zip(values, probs)}

        else:
            parent_values = [bn[p].values for p in parents]

            for combo in product(*parent_values):
                print(f"For parents {parents} = {combo}:")
                probs = input(f"Enter probabilities for {values}: ").split()
                node.cpt[combo] = {v: float(p) for v, p in zip(values, probs)}

        bn[name] = node

    return bn, order


# ----------- MAIN -----------

def main():
    bn, order = build_network()

    print("\n--- Query ---")
    query_var = input("Query variable: ")

    evidence = {}
    e_count = int(input("Number of evidence variables: "))

    for _ in range(e_count):
        var = input("Evidence variable: ")
        val = input(f"Value of {var}: ")
        evidence[var] = val

    result = query(query_var, evidence, bn, order)

    print("\nResult:")
    for k, v in result.items():
        print(f"P({query_var}={k} | evidence) = {v:.5f}")


if __name__ == "__main__":
    main()


#BLOCK WORD PUZZULE

def get_state(name):
    n = int(input(f"Enter number of stacks in {name}: "))
    state = []
    print(f"Enter stacks for {name} (space separated, bottom → top):")
    for i in range(n):
        stack = input(f"Stack {i + 1}: ").split()
        state.append(stack)
    return state


# ----------- HELPERS -----------

def find_block(state, block):
    for i, stack in enumerate(state):
        if block in stack:
            return i, stack.index(block)
    return None, None


def is_clear(state, block):
    i, j = find_block(state, block)
    return j == len(state[i]) - 1


def is_on_table(state, block):
    i, j = find_block(state, block)
    return j == 0


# ----------- OPERATORS -----------

def pickup(state, block, moves):
    # block is on table and clear
    i, j = find_block(state, block)
    state[i].pop()
    if not state[i]:
        state.pop(i)
    moves.append(f"PICKUP({block})")


def putdown(state, block, moves):
    state.append([block])
    moves.append(f"PUTDOWN({block})")


def unstack(state, block, below, moves):
    i, j = find_block(state, block)
    state[i].pop()
    moves.append(f"UNSTACK({block}, {below})")


def stack(state, block, below, moves):
    i, j = find_block(state, below)
    state[i].append(block)
    moves.append(f"STACK({block}, {below})")


# ----------- SOLVER -----------

def solve_block_world(initial, goal):
    moves = []

    # Step 1: Clear everything to table
    blocks = set(b for stack in initial for b in stack)

    for block in blocks:
        while not is_clear(initial, block):
            i, j = find_block(initial, block)
            top = initial[i][-1]
            below = initial[i][-2]

            unstack(initial, top, below, moves)
            putdown(initial, top, moves)

            # Step 2: Build goal
    for stack_goal in goal:
        for i in range(len(stack_goal)):
            block = stack_goal[i]

            # If bottom → ensure on table
            if i == 0:
                if not is_on_table(initial, block):
                    # If on another block → unstack first
                    bi, bj = find_block(initial, block)
                    if bj != 0:
                        below = initial[bi][bj - 1]
                        unstack(initial, block, below, moves)
                    else:
                        pickup(initial, block, moves)

                    putdown(initial, block, moves)

            else:
                below = stack_goal[i - 1]

                # Clear block if needed
                while not is_clear(initial, block):
                    bi, bj = find_block(initial, block)
                    top = initial[bi][-1]
                    bbelow = initial[bi][-2]
                    unstack(initial, top, bbelow, moves)
                    putdown(initial, top, moves)

                    # Move block onto below
                bi, bj = find_block(initial, block)
                if bj == 0:
                    pickup(initial, block, moves)
                else:
                    bbelow = initial[bi][bj - 1]
                    unstack(initial, block, bbelow, moves)

                stack(initial, block, below, moves)

    return moves


# ----------- RUN -----------

initial = get_state("Initial State")
goal = get_state("Goal State")

moves = solve_block_world(initial, goal)

print("\nMoves:")
for m in moves:
    print(m)


#Monkey

from collections import deque

# ----------- VALID POSITIONS -----------

VALID_POSITIONS = ["window", "door", "corner", "center"]
BANANA_POSITION = "ceiling"  # fixed (above center)


# ----------- VALID ACTIONS -----------

def get_next_states(state):
    monkey, box, on_box, has_banana = state
    next_states = []

    # Walk
    if not on_box:
        for p in VALID_POSITIONS:
            if p != monkey:
                next_states.append((
                    (p, box, False, has_banana),
                    f"Monkey walks from {monkey} to {p}"
                ))

                # Push box
    if monkey == box and not on_box:
        for p in VALID_POSITIONS:
            if p != box:
                next_states.append((
                    (p, p, False, has_banana),
                    f"Monkey pushes box from {box} to {p}"
                ))

                # Climb box
    if monkey == box and not on_box:
        next_states.append((
            (monkey, box, True, has_banana),
            "Monkey climbs the box"
        ))

        # Grab banana (ONLY at center under ceiling)
    if monkey == "center" and box == "center" and on_box:
        next_states.append((
            (monkey, box, True, True),
            "Monkey grabs the banana from ceiling"
        ))

    return next_states


# ----------- BFS SEARCH -----------

def bfs(initial):
    queue = deque()
    queue.append((initial, []))
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue
        visited.add(state)

        monkey, box, on_box, has_banana = state

        if has_banana:
            return path

        for new_state, action in get_next_states(state):
            if new_state not in visited:
                queue.append((new_state, path + [action]))

    return None


# ----------- INPUT HANDLER -----------

def get_position(prompt):
    while True:
        pos = input(prompt).strip().lower()
        if pos in VALID_POSITIONS:
            return pos
        else:
            print(f"Invalid! Choose from {VALID_POSITIONS}")

        # ----------- MAIN FUNCTION -----------


def monkey_banana():
    print("\nAvailable positions:", VALID_POSITIONS)
    print("Banana is fixed at: ceiling (above center)\n")

    monkey = get_position("Enter monkey position: ")
    box = get_position("Enter box position: ")

    initial_state = (monkey, box, False, False)

    result = bfs(initial_state)

    print("\nSteps:")
    if result:
        for step in result:
            print(step)
    else:
        print("No solution found")

    # ----------- RUN -----------


if __name__ == "__main__":
    monkey_banana()

