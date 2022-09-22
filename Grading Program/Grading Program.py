student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grade = {}

for name in student_scores:
    score = student_scores[name]
    if score > 90:
        student_grade[name] = "Outstanding"
    elif score > 80:
        student_grade[name] = "Exceeds Expectations"
    elif score > 70:
        student_grade[name] = "Acceptable"
    else:
        student_grade[name] = "Fail"

print(student_grade) 