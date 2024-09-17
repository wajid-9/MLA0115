from collections import deque

def is_valid_state(m_left, c_left, m_right, c_right):
    # Validate the state to ensure no side has more cannibals than missionaries
    if (m_left < 0 or m_left > 3 or c_left < 0 or c_left > 3 or
        m_right < 0 or m_right > 3 or c_right < 0 or c_right > 3):
        return False
    if (m_left > 0 and c_left > m_left) or (m_right > 0 and c_right > m_right):
        return False
    return True

def get_next_states(state):
    m_left, c_left, m_right, c_right, boat = state
    next_states = []
    
    # Define possible moves: (Missionaries to move, Cannibals to move)
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    
    for m, c in moves:
        if boat == 'left':
            new_state = (m_left - m, c_left - c, m_right + m, c_right + c, 'right')
        else:
            new_state = (m_left + m, c_left + c, m_right - m, c_right - c, 'left')
        
        # Validate the new state
        if is_valid_state(new_state[0], new_state[1], new_state[2], new_state[3]):
            next_states.append(new_state)
    
    return next_states

def solve_missionaries_cannibals():
    initial_state = (3, 3, 0, 0, 'left')
    goal_state = (0, 0, 3, 3, 'right')
    
    queue = deque([(initial_state, [])])
    visited = set()
    
    while queue:
        (current_state, path) = queue.popleft()
        
        if current_state == goal_state:
            return path
        
        visited.add(current_state)
        
        for next_state in get_next_states(current_state):
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))
    
    return None

def print_solution(path):
    if path:
        print("Solution found:")
        for state in path:
            print(state)
    else:
        print("No solution found.")

# Example usage
solution_path = solve_missionaries_cannibals()
print_solution(solution_path)
