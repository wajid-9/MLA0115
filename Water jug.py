def water_jug_problem(jug1_cap, jug2_cap, target_amount):
    actions = [("fill", 1), ("fill", 2), ("empty", 1), ("empty", 2), 
               ("pour", 1, 2), ("pour", 2, 1)]
    visited = set()
    path = []
    def explore_states(j1, j2):
        if (j1, j2) in visited:
            return False
        visited.add((j1, j2))
        if j1 == target_amount or j2 == target_amount:
            path.append((j1, j2))
            return True
        for action in actions:
            j1_orig, j2_orig = j1, j2
            if action[0] == "fill":
                if action[1] == 1:
                    j1 = jug1_cap
                else:
                    j2 = jug2_cap
            elif action[0] == "empty":
                if action[1] == 1:
                    j1 = 0
                else:
                    j2 = 0
            elif action[0] == "pour":
                from_jug, to_jug = action[1], action[2]
                if from_jug == 1:
                    amount = min(j1, jug2_cap - j2)
                    j1 -= amount
                    j2 += amount
                else:
                    amount = min(j2, jug1_cap - j1)
                    j2 -= amount
                    j1 += amount
            if explore_states(j1, j2):
                path.append((j1_orig, j2_orig))
                return True
            j1, j2 = j1_orig, j2_orig
        return False
    if explore_states(0, 0):
        print("Solution found:")
        for state in reversed(path):
            print(state)
    else:
        print("No solution found.")
water_jug_problem(4, 3, 2)
