# Isaiah Marshall | Everything completed | "It just works"

def load_data():
    file = open("students.txt", 'r')
    file_lines = file.readlines()
    student_data = []
    for line in file_lines:
        split_line_list = line.split('|')
        student = {
            "name": split_line_list[0],
            "ID": int(split_line_list[1]),
            "credits": int(split_line_list[2]),
            "GPA": float(split_line_list[3])
        }
        student_data.insert(0, student)
    return student_data


def print_menu():
    print("-----------Please select an option below------------")
    print("[1] Add a student to the list.")
    print("[2] Present all Masters students.")
    print("[3] Present all students on probation.")
    print("[4] Present all Honors students.")
    print("[5] Exit the program.")
    print("-----------------------------------------------------")


def perform_command(user_choice, student_data):
    if user_choice == "1":
        add_student(student_data)
    elif user_choice == "2":
        masters_only(student_data)
    elif user_choice == "3":
        probation_only(student_data)
    elif user_choice == "4":
        honors_only(student_data)
    elif user_choice == "5":
        exit(0)
    else:
        print("Invalid selection, please try again.")


def add_student(new_student_data):
    student_name = input("Please enter the new student's name:")
    student_id = int(input(f"Please enter the new student's ID:"))
    student_credits = int(input(f"Please enter the number of Credits the new student has completed:"))
    student_gpa = float(input(f"Please enter the new student's GPA:"))
    student = {
        'name': student_name,
        'ID': student_id,
        'credits': student_credits,
        'GPA': student_gpa
    }
    new_student_data.append(student)


def masters_only(credits_data):
    for students in credits_data:
        if int(students['credits']) < 25:
            masters_students = students
            print(masters_students['name'])


def probation_only(gpa_data):
    for students in gpa_data:
        if float(students['GPA']) < 2.0:
            probation_students = students
            print(probation_students['name'])


def honors_only(gpa_data):
    for students in gpa_data:
        if float(students['GPA']) > 3.0:
            honors_students = students
            print(honors_students['name'])


def main():
    main_student_data = load_data()
    while True:
        print_menu()
        answer = input("Please enter choice 1-4:")
        perform_command(answer, main_student_data)


main()
