import heapq
class PuzzleState:
    def __init__(self, board, moves=0, prev_state=None):
        self.board = board
        self.blank_pos = board.index(0)
        self.moves = moves
        self.prev_state = prev_state
        self.priority = self.moves + self.heuristic()
    def heuristic(self):
        size = int(len(self.board) ** 0.5)
        distance = 0
        for i, tile in enumerate(self.board):
            if tile == 0:
                continue
            target_x, target_y = divmod(tile - 1, size)
            current_x, current_y = divmod(i, size)
            distance += abs(target_x - current_x) + abs(target_y - current_y)
        return distance
    def __lt__(self, other):
        return self.priority < other.priority
    def generate_neighbors(self):
        neighbors = []
        size = int(len(self.board) ** 0.5)
        x, y = divmod(self.blank_pos, size)
        def swap_and_create(new_blank_pos):
            new_board = self.board[:]
            new_board[self.blank_pos], new_board[new_blank_pos] = new_board[new_blank_pos], new_board[self.blank_pos]
            return PuzzleState(new_board, self.moves + 1, self)
        if x > 0:
            neighbors.append(swap_and_create(self.blank_pos - size))
        if x < size - 1:
            neighbors.append(swap_and_create(self.blank_pos + size))
        if y > 0:
            neighbors.append(swap_and_create(self.blank_pos - 1))
        if y < size - 1:
            neighbors.append(swap_and_create(self.blank_pos + 1))
        return neighbors
    def is_goal(self):
        return self.board == list(range(1, len(self.board))) + [0]
def a_star_solver(start_board):
    start_state = PuzzleState(start_board)
    if start_state.is_goal():
        return start_state
    frontier = []
    heapq.heappush(frontier, start_state)
    explored = set()
    explored.add(tuple(start_state.board))
    while frontier:
        current_state = heapq.heappop(frontier)
        if current_state.is_goal():
            return current_state
        for neighbor in current_state.generate_neighbors():
            if tuple(neighbor.board) not in explored:
                explored.add(tuple(neighbor.board))
                heapq.heappush(frontier, neighbor)
    return None
def print_solution(state):
    if state is None:
        print("No solution found!")
        return
    path = []
    while state:
        path.append(state.board)
        state = state.prev_state
    for board in reversed(path):
        print_board(board)
        print()
def print_board(board):
    size = int(len(board) ** 0.5)
    for i in range(size):
        print(" ".join(f"{tile:2}" if tile != 0 else " *" for tile in board[i*size:(i+1)*size]))
    print()
if __name__ == "__main__":
    initial_board = [1, 2, 3, 4, 5, 6, 0, 7, 8]
    solution = a_star_solver(initial_board)
    print_solution(solution)
