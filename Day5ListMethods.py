students_scores = [50, 70, 80, 90, 50, 30, 20, 10, 25, 60]

print("sum: \t\t", sum(students_scores))

total = 0

for score in students_scores:
    total += score

print("sum - manual: \t" , total)

print("max: \t\t", max(students_scores))

max_value = 0

for score in students_scores:
    if score > max_value:
        max_value = score

print("max - manual: \t", max(students_scores))