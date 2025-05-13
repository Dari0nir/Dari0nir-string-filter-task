def filter_strings(array):
    """Фильтрует строки длиной ≤ 3 символа."""
    result = []
    for s in array:
        if len(s) <= 3:
            result.append(s)
    return result

# Пример использования
if __name__ == "__main__":
    input_array = input("Введите строки через запятую: ").split(', ')
    output_array = filter_strings(input_array)
    print(f"Результат: {output_array}")