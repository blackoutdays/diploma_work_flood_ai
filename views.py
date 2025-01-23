import os
import subprocess
from datetime import datetime, timedelta
import random

# Параметры
num_commits = 45  # Количество коммитов
file_name = "fake_commits.txt"  # Файл для фиктивных изменений
start_date = datetime(2024, 11, 1)  # Начало диапазона
end_date = datetime(2025, 1, 31)    # Конец диапазона

# Список сообщений коммитов
commit_messages = [
    "Fix bug in flood prediction algorithm",
    "Improve rainfall data analysis",
    "Add support for new region mapping",
    "Refactor ML model architecture",
    "Optimize data ingestion pipeline",
    "Update dataset schema",
    "Improve test coverage",
    "Add detailed logs for debugging",
    "Enhance API response time",
    "Update documentation for flood analysis",
    "Fix edge case in model prediction",
    "Improve memory efficiency of model",
    "Add example usage scripts",
    "Update system requirements file",
    "Refactor code for better readability",
    "Fix CI/CD deployment issues",
    "Enhance error handling",
    "Add user-friendly UI components",
    "Update notification logic",
    "Improve caching mechanism",
]

# Генерация случайной даты в диапазоне
def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    random_seconds = random.randint(0, 86400)  # 86400 секунд в сутках
    return start + timedelta(days=random_days, seconds=random_seconds)

# Создаем файл, если его нет
if not os.path.exists(file_name):
    open(file_name, 'w').close()

# Создаем коммиты
for i in range(1, num_commits + 1):
    # Генерируем случайную дату
    commit_date = random_date(start_date, end_date)
    formatted_date = commit_date.strftime("%Y-%m-%d %H:%M:%S")

    # Выбираем случайное сообщение для коммита
    commit_message = random.choice(commit_messages)

    # Добавляем фиктивное изменение в файл
    with open(file_name, 'a') as f:
        f.write(f"Commit number {i}: {commit_message}\n")

    # Выводим информацию о коммите
    print(f"Creating commit {i} with date {formatted_date} and message '{commit_message}'")

    # Выполняем команды Git
    subprocess.run(["git", "add", file_name])
    subprocess.run([
        "git", "commit", "-m", commit_message,
        "--date", formatted_date  # Устанавливаем дату коммита
    ])

print(f"All {num_commits} commits created with random dates!")