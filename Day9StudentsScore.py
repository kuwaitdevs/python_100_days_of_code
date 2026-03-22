student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

grades_criteria = [
    {
        'min': 91,
        'max': 100,
        'label': 'Outstanding'
    },
    {
        'min': 81,
        'max': 90,
        'label': 'Exceeds Expectations'
    },
    {
        'min': 71,
        'max': 80,
        'label': 'Acceptable'
    },
    {
        'min': 0,
        'max': 70,
        'label': 'Fail'
    }
]

for student in student_scores:
    for grade_criteria in grades_criteria:
        if student_scores[student] >= grade_criteria['min'] and student_scores[student] <= grade_criteria['max']:
            student_grades[student] = grade_criteria['label']

print(student_grades)