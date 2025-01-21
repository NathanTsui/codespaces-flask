import json

# 讀取 JSON 檔案
with open('students.json', 'r') as file:
    data = json.load(file)

# 處理 JSON 資料
students = data['students']
for student in students:
    name = student['name']
    math_grade = student['grades']['math']
    print(f"Student: {name}, Math Grade: {math_grade}")

# 計算數學平均成績
total_math_grade = 0
for student in students:
    total_math_grade += student['grades']['math']

average_math_grade = total_math_grade / len(students)
print(f"Average Math Grade: {average_math_grade}")