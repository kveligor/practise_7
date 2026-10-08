"""
Кейс-стаді — аналіз CSV-файлу

Ваше завдання — пройти весь шлях від порожньої папки до проєкту на GitHub:

1. Створити папку з проєктом
2. Завантажити туди дані
3. Зробити аналіз
4. Зберегти результат у .txt файл
5. Запушити все на GitHub
"""


# ============================================================
# Крок 1. Створіть папку з проєктом
# ============================================================
# У терміналі:
#
#   mkdir students_analysis
#   cd students_analysis
#
# Усі наступні файли мають лежати всередині цієї папки.


# ============================================================
# Крок 2. Завантажте туди дані
# ============================================================
# Скопіюйте файл students.csv у папку students_analysis.
# Формат файлу: name,math,python,english
# (перший рядок — заголовок, далі по одному студенту в рядку)
#
# Також збережіть цей скрипт у ту саму папку як analyze.py.


# ============================================================
# Крок 3. Зробіть аналіз
# ============================================================
# Потрібно порахувати:
#   - середній бал по класу з кожного предмета (math, python, english);
#   - ім'я студента з найвищим середнім балом (по трьох предметах).

INPUT_FILE = "student_analysis/students.csv"
OUTPUT_FILE = "student_analysis/result.txt"

students_qnt = 0
subjects_sum = []
best_student_avg = -1.0
best_student_name = ""

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    next(f)
    for line in f:
        line = line.strip()
        if not line:
            continue

        parts = line.split(",")
        name = parts[0]
        grades = [float(grade) for grade in parts[1:]]

        students_qnt += 1

        if not subjects_sum:
            subjects_sum = [0.0] * len(grades)

        for i in range(len(grades)):
            subjects_sum[i] += grades[i]

        student_avg = sum(grades) / len(grades)
        if student_avg > best_student_avg:
            best_student_avg = student_avg
            best_student_name = name

math_avg = subjects_sum[0] / students_qnt
python_avg = subjects_sum[1] / students_qnt
english_avg = subjects_sum[2] / students_qnt

result_text = (f"Середній бал по класу:\n"
               f"math: {math_avg:.1f}\n"
               f"python: {python_avg:.1f}\n"
               f"english: {english_avg:.1f}\n\n"
               f"Найкращий студент: {best_student_name} ({best_student_avg:.1f})")


f"Найкращий студент: {best_student_name} ({best_student_avg:.1f})"

with open(OUTPUT_FILE, "w", encoding="utf-8") as out_file:
    out_file.write(result_text)

print(result_text)
#
#   Середній бал по класу:
#   math: 67.8
#   python: 67.9
#   english: 67.9
#
#   Найкращий студент: Ім'я Прізвище (97.0)
#
# Також виведіть цей самий текст на екран через print().
#
# Запустіть скрипт (python analyze.py) і перевірте, що в папці
# з'явився файл result.txt.


# ============================================================
# Крок 5. Запушіть усе на GitHub
# ============================================================
# 1) Створіть новий ПОРОЖНІЙ репозиторій на github.com
#    (без README і .gitignore).
#
# 2) У терміналі, всередині папки students_analysis:
#
git config --global user.email "ihor.kvelenkov.26@kse.org.ua"
git config --global user.name "Ihor Kvelenkov"
git init
git add .
git commit -m "Students analysis"
git branch -M main
git remote add origin https://github.com/kveligor/practise_7.git
git push -u origin main

# 3) Оновіть сторінку репозиторію на GitHub і переконайтеся, що там
#    є students.csv, analyze.py та result.txt.
