def check_symmetry(expression):
    stack = []
    # Словник для відповідності закриваючих дужок відкриваючим
    matching_brackets = {')': '(', ']': '[', '}': '{'}
    
    # Набори відкриваючих та закриваючих дужок для перевірки
    opening = "({["
    closing = ")}]"

    for char in expression:
        # Якщо символ є відкриваючою дужкою, додаємо в стек
        if char in opening:
            stack.append(char)
        
        # Якщо символ є закриваючою дужкою
        elif char in closing:
            # Якщо стек порожній, значить немає відповідної відкриваючої дужки
            if not stack:
                return f"{expression}: Несиметрично"
            
            # Витягуємо останню відкриту дужку зі стеку
            last_open = stack.pop()
            
            # Перевіряємо, чи відповідає вона поточній закриваючій
            if last_open != matching_brackets[char]:
                return f"{expression}: Несиметрично"

    # Після завершення циклу стек має бути порожнім
    if not stack:
        return f"{expression}: Симетрично"
    else:
        return f"{expression}: Несиметрично"

# --- Тестування ---

if __name__ == "__main__":
    test_cases = [
        "( ){[ 1 ]( 1 + 3 )( ){ }}",
        "( 23 ( 2 - 3);",
        "( 11 }",
        "( ( ( )"
    ]

    for text in test_cases:
        print(check_symmetry(text))