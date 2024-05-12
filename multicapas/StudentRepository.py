class StudentRepository:
    def __init__(self):
        self.students = []

    def save_student(self, student):
        self.students.append(student)

    def get_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None