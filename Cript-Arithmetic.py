import itertools

def solve_cryptarithm():
    letters = 'SENDMORY'  # Note the inclusion of 'Y'
    digits = range(10)
    
    # Try all permutations of digits for the letters
    for perm in itertools.permutations(digits, len(letters)):
        letter_to_digit = dict(zip(letters, perm))
        
        # Function to convert a word to a number based on the current letter-to-digit mapping
        def word_to_number(word):
            return int(''.join(str(letter_to_digit[char]) for char in word))
        
        # Convert words to numbers
        send = word_to_number('SEND')
        more = word_to_number('MORE')
        money = word_to_number('MONEY')
        
        # Check if the equation SEND + MORE = MONEY holds
        if send + more == money:
            return letter_to_digit
    
    # Return None if no solution is found
    return None

def print_solution(mapping):
    if mapping:
        print("Solution found:")
        for letter, digit in sorted(mapping.items()):
            print(f"{letter}: {digit}")
    else:
        print("No solution found.")

# Find and print the solution
solution = solve_cryptarithm()
print_solution(solution)
