import json
import os

def fetch_amgu_schedule(group):
    # В будущем здесь будет реальный парсинг через requests и BeautifulSoup
    # Пока возвращаем актуальные предметы для 5104-об
    return [
        "Информационные технологии",
        "Математический анализ",
        "Базы данных",
        "Операционные системы",
        "Основы алгоритмизации"
    ]

# Создаем папку, если ее нет
os.makedirs("data", exist_ok=True)

# Формируем структуру данных
schedule_data = {
    "group": "5104-об",
    "subjects": fetch_amgu_schedule("5104-об")
}

# Сохраняем в JSON
with open("data/schedule.json", "w", encoding="utf-8") as f:
    json.dump(schedule_data, f, ensure_ascii=False, indent=2)

print("Расписание успешно обновлено!")
