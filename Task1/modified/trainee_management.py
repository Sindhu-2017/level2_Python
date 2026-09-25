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

# Display Courses
def get_courses( trainees : list[dict] ) -> set[str]:
    return {
        trainee["trainee_course"]
        for trainee in trainees
    }


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

# Find highest scorers
def get_high_scorers ( trainees : list[dict] ) -> list[dict]:
    return [
        trainee 
        for trainee in trainees
        if trainee["trainee_score"] >= 85
    ]

# Displaying score report
def get_score_report( trainees : list[dict] ) -> dict[str,int]:
    return {
        trainee["trainee_name"] : trainee["trainee_score"]
        for trainee in trainees
    }

# sort by score
def sort_by_score ( trainees : list[dict] ) -> list[dict]:
    return sorted(
        trainees,
        key = lambda trainee :trainee["trainee_score"],
        reverse=True

    )

def all_have_good_score ( trainees : list[dict] ) -> bool:
    return all(
        trainee["trainee_score"] >= 70
        for trainee in trainees
    )

def has_top_performer ( trainees : list[dict] ) -> bool:
    return any(
        trainee["trainee_score"] >= 90
        for trainee in trainees
    )

while True :
    print("1. Add Trainee")
    print("2. Display All Trainees")
    print("3. Display Courses")
    print("4. Filter by Course")
    print("5. Display High Performers")
    print("6. Search Trainee by Name")

    print("7. Display Score Report")
    print("8. Sort Trainees by Score")
    print("9. Check All trainees have good score")
    print("10. Check whether any trainee is topper")
    print("11. Exit")
    choice = int(input("Enter your choice :"))

    match choice :
        case 1:
            print("1. Add Trainee")
            add_trainee(trainees)

        case 2:
            print("2. Display All Trainees")
            display_trainees(trainees)

        case 3:
            print("3. Display Courses")
            courses = get_courses(trainees)
            for course in courses:
                print(course)
            
        case 4:
            print("4. Filter by Course")
            course : str = input ("Enter the course to filter :")
            filtered_result : list[dict] = filter_by_course(trainees,course)

            if filtered_result :
                display_trainees(filtered_result)
            else:
                print("No trainees found")

        case 5:
            print("5. Display High Scorers")
            highest_scorers = get_high_scorers (trainees) 
            display_trainees(highest_scorers)

        case 6:
            print("6. Search Trainee by Name")
            name : str = input ("Enter the name to search :")
            result :list[dict] = search_trainee(trainees,name)
                        
            if result :
                display_trainees(result)
            else:
                print("Trainee not found")

        case 7:
            print("Display Score Report")
            score_report = get_score_report(trainees)
            for trainee_name,trainee_score in score_report.items():
                print(f"{trainee_name} :{trainee_score}")

        case 8:
            print("8. Sort Trainees by Score")
            sorted_trainees = sort_by_score(trainees)
            display_trainees(sorted_trainees)

        case 9:
            print("9. Check All trainees have good score")
            all_good = all_have_good_score(trainees)
            print(f"All trainees have score >= 70 : {all_good}")

        case 10:
            print("10. Check whether any trainee is topper")
            top_performer = has_top_performer(trainees)
            print(f"At least one trainee has score >= 90: {top_performer}")

        case 11:
            print("Exiting..")
            break
        case _:
            print("Invalid choice")