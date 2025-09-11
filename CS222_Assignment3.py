
def get_students(student):
    students = {}
    try: 
        with open(student, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    studentId,lastName, firstName, major, gpa = line.split(",")
                    students[studentId] = [lastName, firstName, major, gpa]
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        exit(1)
    return students

def search_by_lastname(students, last_name):
    results = [
        (student, info) for student, info in students.items()
        if info[0].lower() == last_name.lower()
    ]
    if results:
        for student, info in results:
            print(f"ID: {student}, Last Name: {info[0]}, First Name: {info[1]}, Major: {info[2]}, GPA: {info[3]}")
    else:
        print("No student found with that last name.")


def search_by_major(students, major):
    """Find and print students by major."""
    results = [
        (student, info) for student, info in students.items()
        if info[2].lower() == major.lower()
    ]
    if results:
        for student, info in results:
            print(f"ID: {student}, Last Name: {info[0]}, First Name: {info[1]}, Major: {info[2]}, GPA: {info[3]}")
    else:
        print("No student found with that major.")


def main():
    students = load_students("students.txt")

    while True:
        print("\nChoose an option:")
        print("1) Search by Last Name")
        print("2) Search by Major")
        print("3) Quit")

        choice = input("Enter choice: ")

        if choice == "1":
            last_name = input("Enter last name to search for: ")
            search_by_lastname(students, last_name)
        elif choice == "2":
            major = input("Enter major to search for: ")
            search_by_major(students, major)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()

