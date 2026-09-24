trainees = [
    {
        "trainee_name": "Arun",
        "trainee_course": "Python",
        "trainee_score": 85,
        "trainee_attendance": 92
    },
    {
        "trainee_name": "Priya",
        "trainee_course": "Automation Testing",
        "trainee_score": 92,
        "trainee_attendance": 88
    },
    {
        "trainee_name": "Kumar",
        "trainee_course": "Python",
        "trainee_score": 78,
        "trainee_attendance": 95
    },
    {
        "trainee_name": "Divya",
        "trainee_course": "AI QA",
        "trainee_score": 88,
        "trainee_attendance": 90
    },
    {
        "trainee_name": "Ravi",
        "trainee_course": "Automation Testing",
        "trainee_score": 68,
        "trainee_attendance": 75
    }
]


# Add Trainee
def add_trainee(trainees : list[dict]) -> None :
    name :str = input("Enter trainee name :")
    course :str = input("Enter course :")
    score :int = int(input("Enter Score :"))
    attendance:int =  int(input("Enter attendance :"))

    trainees.append ({
            "trainee_name": name,
            "trainee_course": course,
            "trainee_score": score,
            "trainee_attendance": attendance
        })

    print("Trainee Added Sucessfully...")

# Displaying all trainees
def display_trainees( trainees : list [dict]) -> None :

    for number ,trainee in enumerate (trainees ,start=1):

        print (f"{number} . {trainee['trainee_name']} - {trainee['trainee_course']} - Score : {trainee['trainee_score']} - Attendance : {trainee['trainee_attendance']}")


# Search Trainee
def search_trainee (trainees : list[dict] , name :str) -> list[dict]:

    return[
        trainee
        for trainee in trainees
        if trainee["trainee_name"].lower() == name.lower()
    ]

# filter by course
def filter_by_course(trainees :list[dict] , course : str) ->list[dict]:
    return[
        trainee
        for trainee in trainees
        if trainee["trainee_course"].lower() == course.lower()
    ]

# def calculate_average_score(trainees :list[dict] , course : str) -> float:



while True :
    print("1. Add Trainee")
    print("2. Display All Trainees")
    print("3. Search Trainee by Name")
    print("4. Filter by Course")
    print("5. Calculate Average Score")
    print("6. Find Highest Scorer")
    print("7. Count Pass / Fail")
    print("8. Attendance Warnings")
    print("9. Generate Summary")
    print("10. Sort by Attendance")
    print("11. Display Courses")
    print("12. Check Attendance")
    print("13. Exit")
    choice = int(input("Enter your choice :"))

    match choice :
        case 1:
            print("1. Add Trainee")
            add_trainee(trainees)

        case 2:
            print("2. Display All Trainees")
            display_trainees(trainees)

        case 3:
            print("3. Search Trainee by Name")
            name : str = input ("Enter the name to search :")
            result :list[dict] = search_trainee(trainees,name)
            
            if result :
                display_trainees(result)
            else:
                print("Trainee not found")

        case 4:
            print("4. Filter by Course")
            course : str = input ("Enter the course to filter :")
            filtered_result : list[dict] = filter_by_course(trainees,course)

            if filtered_result :
                display_trainees(filtered_result)
            else:
                print("No trainees found")

        case 5:
            print("5. Calculate Average Score")
            average_result = calculate_average_score (trainees) 
            print(f"Average Score : {average_result}")

        case 13:
            print("Exiting..")
            break
        case _:
            print("Invalid choice")


