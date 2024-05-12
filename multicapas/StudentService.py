class StudentService:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None