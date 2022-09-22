student_scores = input('Input a list of student scores: ').split()
max = 0

for i in range(len(student_scores)):
    student_scores[i] = int(student_scores[i])

for score in student_scores:
    if score > max:
        max = score
print(f'The highest score is {max}')