students=[
    {"id":101,"name":"johnson","department":"cs"},
    {"id":102,"name":"johnson","department":"cs"},
    {"id":103,"name":"johnson","department":"cs"}
]
while True:
    choice=int(input("1. Add a name\n2. Display names\n3. Edit a name\n4. Delete a name\n5. Exit\nEnter your choice: "))
    match choice:
        case 1:
            name=input("Enter a name: ")
            std_id=int(input("enter the id: "))
            department=input("enter department: ")
            students.append({"id":std_id,"name":name,"department":department})
        case 2:
            print(f"{'ID':^4}{'Name':^10}{'Department':^10}")
            print('-'*25)
            for student in students:
                print(f"{student['id']:<4}{student['name']:<10}{student['department']:<10}")
            print('-'*25)
            print(f"Total count: {len(students):>7}")
        case 3:
            print(f"{'ID':^4}{'Name':^10}{'Department':^10}")
            print('-'*25)
            for student in students:
                print(f"{student['id']:<4}{student['name']:<10}{student['department']:<10}")
            print('-'*25)
            id = int(input("Enter the id of the student that you want to edit: "))
            edit_student=None
            for student in students:
                if student['id'] == id:
                    edit_student = student
            edit_student['name']=input("enter the new name: ")
            edit_student['department']=input("enter the new deprtment:")
            
        case 4:
            print(f"{'ID':^4}{'Name':^10}{'Department':^10}")
            print('-'*25)
            for student in students:
                print(f"{student['id']:<4}{student['name']:<10}{student['department']:<10}")
            print('-'*25)
            edit_student = None
            for student in students:
                if student['id'] == id:
                    edit_student = student
            delete_student = int(input("Enter the id of the student you want to delete:"))
            print(students.pop(delete_student))
        case 5:
            break
        case _:
            print("Invalid entry")