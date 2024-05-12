import Student
import StudentRepository
import StudentService
def main():
    student_service = StudentService.StudentService()
    student_repository = StudentRepository.StudentRepository()

    while True:
        print("\n1. Agregar estudiante")
        print("2. Buscar estudiante por ID")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del estudiante: ")
            edad = input("Ingrese la edad del estudiante: ")
            id_estudiante = len(student_repository.students) + 1
            nuevo_estudiante = Student.Student(nombre, edad, id_estudiante)
            student_service.add_student(nuevo_estudiante)
            student_repository.save_student(nuevo_estudiante)
            print("Estudiante agregado con éxito.")

        elif opcion == "2":
            id_estudiante = int(input("Ingrese el ID del estudiante a buscar: "))
            estudiante = student_service.find_student_by_id(id_estudiante)
            if estudiante:
                print(f"Nombre: {estudiante.name}, Edad: {estudiante.age}")
            else:
                print("Estudiante no encontrado.")

        elif opcion == "3":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()