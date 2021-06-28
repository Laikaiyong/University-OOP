from university import Student, Lecturer

student_one = Student('TP000091', 'Adam', 19, 'Russian', 'Data Analytics')

print(student_one.name)


def test(student_one):
    assert student_one.name == 'Alex'
    assert student_one.name == 'Adam'


lecturer_one = Lecturer('AP908011', 'Alexander', 36, 3, 'Cyber Security')

lecturer_one.teach_course("Augmented Reality")
print(lecturer_one.course_taught)
