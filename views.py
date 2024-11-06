import os
import subprocess
from datetime import datetime, timedelta, timezone
import random

# Параметры
num_commits = 45
file_name = "fake_commits.txt"
start_date = datetime(2024, 10, 1, tzinfo=timezone.utc)  # Начало диапазона
end_date = datetime(2025, 1, 31, tzinfo=timezone.utc)    # Конец диапазона

commit_messages = [
    "Fix flood prediction algorithm",
    "Improve water level monitoring",
    "Add new visualization for flood zones",
    "Optimize rainfall data analysis",
    "Refactor pipeline for performance",
]

# Генерация случайной даты в UTC
def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    random_seconds = random.randint(0, 86400)  # 86400 секунд в сутках
    return start + timedelta(days=random_days, seconds=random_seconds)

if not os.path.exists(file_name):
    open(file_name, 'w').close()

for i in range(1, num_commits + 1):
    commit_date = random_date(start_date, end_date)
    formatted_date = commit_date.isoformat()  # Дата в формате ISO-8601

    commit_message = random.choice(commit_messages)

    with open(file_name, 'a') as f:
        f.write(f"Commit number {i}: {commit_message}\n")

    subprocess.run(["git", "add", file_name])
    subprocess.run([
        "git", "commit", "-m", commit_message,
        "--date", formatted_date
    ])

print(f"All {num_commits} commits created with random UTC dates!")