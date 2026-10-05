import heapq

def heuristic(state, goal):
    count = 0

    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1

    return count


def get_neighbors(state):
    neighbors = []

    zero = state.index(0)

    row = zero // 3
    col = zero % 3

    moves = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_zero = new_row * 3 + new_col

            new_state = list(state)

            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors


def print_state(state):
    print(state[0], state[1], state[2])
    print(state[3], state[4], state[5])
    print(state[6], state[7], state[8])


def a_star(start, goal):

    pq = []

    g = 0
    h = heuristic(start, goal)
    f = g + h

    heapq.heappush(
        pq,
        (f, g, start, [start])
    )

    best_g = {start: 0}
    expanded = set()
    count = 0

    while pq:

        f, g, current, path = heapq.heappop(pq)

        if current in expanded:
            continue

        expanded.add(current)

        h = heuristic(current, goal)

        count += 1

        print()
        print("Expanded State", count)
        print_state(current)
        print("g(n) =", g)
        print("h(n) =", h)
        print("f(n) =", g + h)

        if current == goal:
            return path

        for neighbor in get_neighbors(current):

            new_g = g + 1

            if neighbor not in best_g or new_g < best_g[neighbor]:

                best_g[neighbor] = new_g

                new_h = heuristic(neighbor, goal)
                new_f = new_g + new_h

                heapq.heappush(
                    pq,
                    (
                        new_f,
                        new_g,
                        neighbor,
                        path + [neighbor]
                    )
                )

    return None


start_input = input("Enter initial state (use 0 for blank): ")
goal_input = input("Enter goal state (use 0 for blank): ")

start = tuple(map(int, start_input.split()))
goal = tuple(map(int, goal_input.split()))

if len(start) != 9 or len(goal) != 9:

    print("Please enter exactly 9 numbers.")

else:

    print()
    print("========== A* SEARCH ==========")

    solution = a_star(start, goal)

    if solution is None:

        print()
        print("No solution exists.")

    else:

        print()
        print("========== FINAL PATH ==========")
        print()

        for i, state in enumerate(solution):

            g = i
            h = heuristic(state, goal)
            f = g + h

            print("Step", i)
            print_state(state)
            print("g(n) =", g)
            print("h(n) =", h)
            print("f(n) =", f)
            print()

        print("Total moves =", len(solution) - 1)

    print()
    print("================================")
    print("Name : Anish Nagpal")
    print("USN  : 1WN24CS040")
    print("================================")
