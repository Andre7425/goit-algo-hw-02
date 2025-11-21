from collections import deque


def is_palindrome(input_string):
    """
    Перевіряє, чи є рядок паліндромом, використовуючи deque.
    Ігнорує регістр та пробіли.
    """
    # 1. Попередня обробка рядка:
    # Приводимо до нижнього регістру та видаляємо пробіли
    formatted_string = input_string.lower().replace(" ", "")
    
    # 2. Створюємо двосторонню чергу (deque)
    # та додаємо всі символи рядка до неї
    char_deque = deque(formatted_string)
    
    # 3. Порівнюємо символи з обох кінців
    # Продовжуємо, поки в черзі більше 1 елемента.
    # (Якщо залишиться 0 або 1 символ — це автоматично успіх)
    while len(char_deque) > 1:
        # Видаляємо (pop) елемент з лівого краю
        left_char = char_deque.popleft()
        # Видаляємо (pop) елемент з правого краю
        right_char = char_deque.pop()
        
        # Якщо символи не співпадають — це не паліндром
        if left_char != right_char:
            return False
            
    # Якщо цикл завершився без повернення False, значить рядок є паліндромом
    return True

# --- Тестування програми ---


if __name__ == "__main__":
    test_cases = [
        "Anna",                 # Парна кількість, різний регістр
        "Civic",                # Непарна кількість
        "A man a plan a canal Panama", # Пробіли та регістр
        "Hello World",          # Не паліндром
        "12321",                # Числа (як рядок)
        "Noon"                  # Парна кількість
    ]

    print("Перевірка на паліндром:\n")
    for text in test_cases:
        result = is_palindrome(text)
        status = "✅ Паліндром" if result else "❌ Не паліндром"
        print(f"'{text}' -> {status}")