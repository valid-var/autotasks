def analyze_students(data: dict, threshold: int = 75) -> dict:
    """
    Анализирует данные об оценках студентов.

    Параметры:
    - data (dict): Словарь с именами студентов (ключи) и списками их оценок (значения).
    - threshold (int): Порог среднего балла для отбора студентов (по умолчанию 75).

    Возвращает:
    - dict: Словарь с результатами анализа:
        - "average_scores": Словарь со средними баллами каждого студента.
        - "top_student": Имя студента с наивысшим средним баллом.
        - "above_threshold": Список студентов, чей средний балл выше порога.
    """
    pass


def test_analyze_students():
    students = {
        "Alice": [85, 90, 78],
        "Bob": [60, 70, 65],
        "Carol": [88, 92, 95],
        "Dave": [72, 68, 70]
    }

    result = analyze_students(students, threshold=75)

    expected_result = {
        "average_scores": {
            "Alice": 84.33,
            "Bob": 65.0,
            "Carol": 91.67,
            "Dave": 70.0
        },
        "top_student": "Carol",
        "above_threshold": ["Alice", "Carol"]
    }

    assert result == expected_result, f"Ожидалось: {expected_result}, Получено: {result}"
    print("Все тесты пройдены.")


# Запуск тестов
test_analyze_students()