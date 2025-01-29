import pandas as pd

import os

# defining the file paths for the students, courses, and grades data
students_file = "C:\\Users\\cnorr\\OneDrive\\Desktop\\Winter 2025\\CS290 DataBase\\Lab1\\students .csv"
courses_file = "C:\\Users\\cnorr\\OneDrive\\Desktop\\Winter 2025\\CS290 DataBase\\Lab1\\courses.csv"
grades_file = "C:\\Users\\cnorr\\OneDrive\\Desktop\\Winter 2025\\CS290 DataBase\\Lab1\\grades.csv"

students_headers = ['id', 'last_name', 'first_name', 'phone', 'email']
courses_headrers = ['name', 'semester', 'code']
grades_headers = ['id', 'last_name', 'first_name', 'CS2020_W', 'CS2020_F', 'CS2040_F', 'CS2910_W']



# loading the csv files into pandas DataFrames, using ";" as the delimiter
students = pd.read_csv(students_file, delimiter=";", header = None, names = students_headers)  # loads student data into a DataFrame and applys the header
courses = pd.read_csv(courses_file, delimiter=";", header = None, names = courses_headrers)    # loads course data into a DataFrame and applys the header
grades = pd.read_csv(grades_file, delimiter=";", header = None, names = grades_headers)      # loads grades data into a DataFrame and applys the header


# saves the modified DataFrames back to their respective csv files
def save_data():
    # ensure the students file ends with a newline and append new rows
    # open the students file in append mode
    with open(students_file, "a") as f:
        f.write("\n")  # add a newline to the file if it's missing
    # write the last row of the students dataframe to the file without the header
    students.iloc[-1:].to_csv(students_file, sep=";", index=False, header=False, mode="a")

    # ensure the grades file ends with a newline and append new rows
    # open the grades file in append mode
    with open(grades_file, "a") as f:
        f.write("\n")  # add a newline to the file if it's missing
    # write the last row of the grades dataframe to the file without the header
    grades.iloc[-1:].to_csv(grades_file, sep=";", index=False, header=False, mode="a")

    # ensure the courses file ends with a newline and append new rows
    # open the courses file in append mode
    with open(courses_file, "a") as f:
        f.write("\n")  # add a newline to the file if it's missing
    # write the last row of the courses dataframe to the file without the header
    courses.iloc[-1:].to_csv(courses_file, sep=";", index=False, header=False, mode="a")

# displays a DataFrame with a title
def display_df(df, title):
    print(f"\n{title}")  # prints the title
    print(df.to_string(index=False))  # converts the DataFrame to a string and displays it without the index

# outputs the list of all students
def output_stduents():
    display_df(students, "\nOriginal List of All Students\n")  # uses display_df to show the students DataFrame

# sorts the students by last name in ascending or descending order based on user input
def sort_student():
    while True:
        sort_alphabetically = input(
            "\nDo you want the list alphabetically or reverse alphabetical?\n"
            "Enter A for alphabetically or R for reverse alphabetical: "
        ).strip().lower()  # gets user input and converts it to lowercase
        if sort_alphabetically == "r":
            # sorts by "last_name" in descending order and displays it
            sorted_students = students.sort_values(by="last_name", ascending=True)
            display_df(sorted_students, "Students Sorted by Name (Reverse)")
            break  # exits the loop
        elif sort_alphabetically == "a":
            # sorts by "last_name" in ascending order and displays it
            sorted_students = students.sort_values(by="last_name", ascending=False)
            display_df(sorted_students, "Students Sorted by Name")
            break  # exits the loop
        else:
            print("Invalid input. Please enter 'A' or 'R'.")  # prompts user for valid input

# outputs the list of all courses
def output_course():
    display_df(courses, "\nOriginal List of All Courses")  # displays the courses DataFrame

# filters and displays courses by semester
def course_by_semester():
    semester = input("\nEnter semester: ").strip()  # gets the semester input
    semester_courses = courses[courses["semester"].str.strip() == semester]  # filters courses DataFrame by semester
    if semester_courses.empty:
        print(f"No courses found for semester: {semester}")  # message if no courses are found
    else:
        display_df(semester_courses, f"Courses for Semester: {semester}")  # displays filtered courses

# filters courses by semester and sorts them by name
def course_by_semester_sorted():
    # prompts the user to input a semester and verifies it is valid
    while True:
        semester = input("\nEnter semester (fall, winter, spring): ").strip().lower()
        if semester in ["fall", "winter", "spring"]:
            break
        print("Invalid semester. Please enter 'fall', 'winter', or 'spring'.")  # prompts for valid semester

    # gets user input for sorting order
    sort_order = input(
        "\nDo you want the courses alphabetically or reverse alphabetically?\n"
        "Enter A for alphabetically or R for reverse alphabetical: "
    ).strip().lower()

    # filters courses DataFrame by semester
    semester_courses = courses[courses["semester"].str.strip().str.lower() == semester]

    if semester_courses.empty:
        print(f"No courses found for semester: {semester}")  # message if no courses are found
        return

    if sort_order == "r":
        # sorts by "name" in descending order and displays it
        sorted_courses = semester_courses.sort_values(by="name", ascending=False)
        display_df(sorted_courses, f"Courses for Semester: {semester} (Reverse Alphabetical)")
    elif sort_order == "a":
        # sorts by "name" in ascending order and displays it
        sorted_courses = semester_courses.sort_values(by="name", ascending=True)
        display_df(sorted_courses, f"Courses for Semester: {semester} (Alphabetical)")
    else:
        print("Invalid input. Please enter 'A' or 'R'.")  # prompts user for valid input


# adds a new student to the students and grades dataframes and updates the corresponding files.
# ensures no duplicate student id is added and initializes grades for the new student as 'na'.
def add_new_student():
    global students, grades

    while True:
        # prompt the user for a new student id and validate it
        while True:
            new_id = input("\nEnter student ID (numbers only): ").strip()
            if new_id.isdigit():
                break
            print("Invalid ID. Please enter numbers only.")

        # check if the student id already exists
        if new_id in students["id"].values:
            print(f"Error: A student with ID {new_id} already exists.")

            # ask the user if they want to retry adding the student
            retry = input("\nDo you want to try again? (yes to retry / no to exit): ").strip().lower()
            if retry != "yes":  # exit if the user doesn't want to retry
                print("Exiting student addition.")
                break
        else:
            # collect and validate new student details from the user
            while True:
                last_name = input("Enter last name (letters only): ").strip()
                if last_name.isalpha():
                    break
                print("Invalid last name. Please enter letters only.")

            while True:
                first_name = input("Enter first name (letters only): ").strip()
                if first_name.isalpha():
                    break
                print("Invalid first name. Please enter letters only.")

            while True:
                phone = input("Enter phone number (numbers only): ").strip()
                if phone.isdigit():
                    break
                print("Invalid phone number. Please enter numbers only.")

            while True:
                email = input("Enter email address (must contain '@'): ").strip()
                if "@" in email:
                    break
                print("Invalid email. Please include '@' in the address.")

            # prepare the new student details
            new_student = {
                "id": new_id,  # set the student id
                "last_name": last_name,  # set the last name
                "first_name": first_name,  # set the first name
                "phone": phone,  # set the phone number
                "email": email  # set the email address
            }

            # append the new student to the students dataframe
            students = pd.concat([students, pd.DataFrame([new_student])], ignore_index=True)

            # ensure the students file ends with a newline before appending the new student
            with open(students_file, "a") as f:
                f.write("\n")  # add a newline if missing
            # write the new student record to the students file without a header
            students.iloc[-1:].to_csv(students_file, sep=";", index=False, header=False, mode="a")

            # create a new row for the student in the grades dataframe
            new_grades_entry = {col: "na" for col in grades.columns}  # set all columns to 'na' by default
            new_grades_entry["id"] = new_id  # set the id
            new_grades_entry["last_name"] = new_student["last_name"]  # set the last name
            new_grades_entry["first_name"] = new_student["first_name"]  # set the first name

            # append the new grades row to the grades dataframe
            grades = pd.concat([grades, pd.DataFrame([new_grades_entry])], ignore_index=True)

            # ensure the grades file ends with a newline before appending the new grades row
            with open(grades_file, "a") as f:
                f.write("\n")  # add a newline if missing
            # write the new grades record to the grades file without a header
            grades.iloc[-1:].to_csv(grades_file, sep=";", index=False, header=False, mode="a")

            # confirm successful addition
            print("Student added successfully to both students and grades files!")
            break


# adds a new course to the courses and grades dataframes and updates the corresponding files.
# the course name is appended with '_F' or '_W' based on the semester (fall or winter).
# ensures no duplicate courses are added and initializes grades for the new course as 'na' for all students.
def add_new_course():
    global courses, grades, grades_headers

    try:
        # prompt the user to enter the course name and semester
        course_name = input("\nEnter the course name: ").strip().upper()  # convert course name to uppercase
        semester = input("Enter the semester (Fall/Winter): ").strip().capitalize()  # capitalize the semester

        # determine the suffix for the grades_headers entry based on the semester
        if semester == "Fall":
            grades_course_name = f"{course_name}_F"  # append '_F' for fall
        elif semester == "Winter":
            grades_course_name = f"{course_name}_W"  # append '_W' for winter
        else:
            print("Error: Invalid semester. Please enter 'Fall' or 'Winter'.")
            return  # exit the function if the semester is invalid

        # check if the course already exists in grades_headers
        if grades_course_name in grades_headers:
            print(f"Error: The course '{grades_course_name}' already exists.")
        else:
            # add the course to grades_headers with the appropriate suffix
            grades_headers.append(grades_course_name)

            # ensure the 'code' column in courses is numeric and find the next available code
            courses['code'] = pd.to_numeric(courses['code'], errors='coerce').fillna(0).astype(int)
            new_code = courses['code'].max() + 1  # increment the maximum code by 1

            # create the new course entry as a DataFrame
            new_course_entry = pd.DataFrame([{
                "name": course_name,  # course name without the suffix
                "semester": semester,  # the semester (fall or winter)
                "code": new_code  # the new unique code for the course
            }])
            # append the new course to the courses dataframe
            courses = pd.concat([courses, new_course_entry], ignore_index=True)

            # append the new course to the courses file
            with open(courses_file, "a") as f:
                f.write("\n")  # add a newline if the file doesn't end with one
            new_course_entry.to_csv(courses_file, sep=";", index=False, header=False, mode="a")

            # update the grades dataframe to include the new course
            grades[grades_course_name] = "na"  # initialize all grades for the new course as 'na'

            # save the updated grades file and reload it with updated headers
            grades.to_csv(grades_file, sep=";", index=False, header=False, mode="w")  # write the updated grades to the file
            grades = pd.read_csv(grades_file, delimiter=";", header=None, names=grades_headers)  # reload grades with headers

            # confirm successful addition
            print(f"Course '{grades_course_name}' added successfully with code '{new_code}'!")
    except Exception as e:
        # handle any exceptions that occur and display the error
        print(f"An error occurred while adding the course: {e}")

# adds or updates a grade for a specific student in a specific course.
# validates the student id and course name before updating.
# updates the grades dataframe and saves the changes directly to the grades file.
def add_or_update_grade():
    global grades, grades_headers

    try:
        # ensure the 'id' column is treated as a string for consistent comparison
        grades["id"] = grades["id"].astype(str)

        # prompt the user for the student id and validate it
        while True:
            student_id = input("\nEnter the student ID (numbers only): ").strip()
            if student_id.isdigit():
                break
            print("Invalid ID. Please enter numbers only.")

        # check if the student id exists in the grades dataframe
        if student_id not in grades["id"].values:
            print(f"Error: No student found with ID {student_id}.")
        else:
            # prompt the user for the course name and semester
            course_name = input("Enter the course name: ").strip().upper()  # convert course name to uppercase
            semester = input("Enter the semester: ").strip()  # keep semester case flexible
            course_full_name = f"{course_name}_{semester[0].upper()}"  # format as CS2020_W or CS2020_F

            # check if the course exists in grades_headers
            if course_full_name not in grades_headers:
                print(f"Error: Course '{course_full_name}' does not exist. Please add it first.")
            else:
                # prompt the user for the new grade and validate it
                while True:
                    new_grade = input(f"Enter the grade for {course_full_name} (numbers only): ").strip()
                    if new_grade.isdigit():
                        break
                    print("Invalid grade. Please enter numbers only.")

                # update the grade for the specific student and course in the grades dataframe
                grades.loc[grades["id"] == student_id, course_full_name] = new_grade

                # save the updated grades dataframe to the grades file without the header
                grades.to_csv(grades_file, sep=";", index=False, header=False)

                # confirm successful grade update
                print(f"Grade updated for student ID {student_id} in course '{course_full_name}'.")
    except Exception as e:
        # handle and display any errors that occur during the process
        print(f"An error occurred while updating the grade: {e}")


# displays a menu of actions for the user to perform, such as adding a student, adding a course, or updating grades.
# executes the corresponding function based on the user's input and handles invalid input gracefully.
# provides an option to exit the program.
def get_user_action():
    while True:
        # display the menu of options to the user
        print("\nWhat would you like to do?")
        print("1: Add a new student")  # option to add a new student
        print("2: Add a new course")  # option to add a new course
        print("3: Add or update a grade")  # option to add or update a grade
        print("4: Exit")  # option to exit the program

        try:
            # prompt the user for their choice
            action = int(input("Enter your choice (1, 2, 3, or 4): ").strip())

            # handle the user's choice
            if action == 1:
                add_new_student()  # call the function to add a new student
            elif action == 2:
                add_new_course()  # call the function to add a new course
            elif action == 3:
                add_or_update_grade()  # call the function to add or update a grade
            elif action == 4:
                # exit the program
                print("Exiting the program.")
                break
            else:
                # handle invalid numerical input outside the range 1-4
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            # handle non-numerical input
            print("Invalid input. Please enter a number between 1 and 4.")

# updates information for an existing student in the students dataframe.
# allows updating of last name, first name, phone, and email while retaining unchanged fields.
# updates both the students and grades files directly without adding headers.
def update_student_info():
    # prompt the user to enter the student id they want to update and validate it
    while True:
        student_id = input("\nEnter the student ID to update (numbers only): ").strip()
        if student_id.isdigit():
            break
        print("Invalid ID. Please enter numbers only.")

    # check if the student id exists in the students dataframe
    if student_id in students["id"].astype(str).values:
        # inform the user about the update process
        print("Enter new values for the student. Press Enter to keep the current value.")

        # fetch the current values for the student
        current_student = students[students["id"].astype(str) == student_id].iloc[0]

        # validate and prompt for last name
        while True:
            new_last_name = input(f"Current Last Name ({current_student['last_name']}): ").strip()
            if not new_last_name or new_last_name.isalpha():
                break
            print("Invalid last name. Please enter letters only.")

        # validate and prompt for first name
        while True:
            new_first_name = input(f"Current First Name ({current_student['first_name']}): ").strip()
            if not new_first_name or new_first_name.isalpha():
                break
            print("Invalid first name. Please enter letters only.")

        # validate and prompt for phone number
        while True:
            new_phone = input(f"Current Phone ({current_student['phone']}): ").strip()
            if not new_phone or new_phone.isdigit():
                break
            print("Invalid phone number. Please enter numbers only.")

        # validate and prompt for email
        while True:
            new_email = input(f"Current Email ({current_student['email']}): ").strip()
            if not new_email or "@" in new_email:
                break
            print("Invalid email. Please include '@' in the address.")

        # ensure the 'phone' column is treated as a string to avoid dtype conflicts
        students["phone"] = students["phone"].astype(str)

        # update the last name, first name, phone, and email fields with new values or retain the existing ones
        students.loc[students["id"].astype(str) == student_id, "last_name"] = new_last_name or current_student["last_name"]
        students.loc[students["id"].astype(str) == student_id, "first_name"] = new_first_name or current_student["first_name"]
        students.loc[students["id"].astype(str) == student_id, "phone"] = new_phone or current_student["phone"]
        students.loc[students["id"].astype(str) == student_id, "email"] = new_email or current_student["email"]

        # save the updated students dataframe back to the file without headers
        students.to_csv(students_file, sep=";", index=False, header=False)

        # check if the student also exists in the grades dataframe
        if student_id in grades["id"].astype(str).values:
            # save the updated grades dataframe back to the file without headers
            grades.to_csv(grades_file, sep=";", index=False, header=False)

        # confirm the update to the user
        print("Student information updated successfully!")
    else:
        # display a message if the student id is not found
        print("No student found with that ID.")


# searches for a course by name
def search_course_by_name():
    course_name = input("\nEnter course name: ").strip()  # gets the course name
    result = courses[courses["name"].str.contains(course_name, case=False, na=False)]  # filters by course name
    if result.empty:
        print(f"No course found with name: {course_name}")  # message if no course is found
    else:    
        display_df(result, f"Search Results for Course Name: {course_name}")  # displays the matching courses

# searches for a course by code
def search_course_by_code():
    while True:
        course_code = input("\nEnter course code (numbers only): ").strip()  # gets the course code
        if course_code.isdigit():
            break  # valid input, exit the loop
        print("Invalid input. Course code should contain numbers only.")  # error message for invalid input

    # filters by code
    result = courses[courses["code"].astype(str).str.contains(course_code, case=False, na=False)]
    if result.empty:
        print(f"No course found with code: {course_code}")  # message if no course is found
    else:
        display_df(result, f"Search Results for Course Code: {course_code}")  # displays the matching courses



# searches for a student by last name
def search_student_by_last_name():
    while True:
        last_name = input("\nEnter last name: ").strip()  # gets the last name
        if last_name.isalpha():
            break  # valid input, exit the loop
        print("Invalid input. Last name should contain letters only.")  # error message for invalid input

    # filters by last name
    result = students[students["last_name"].str.contains(last_name, case=False, na=False)]
    if result.empty:
        print(f"No student found with Last Name: {last_name}")  # message if no student is found
    else:    
        display_df(result, f"Search Results for Last Name: {last_name}")  # displays the matching students


# searches for a student by phone number
def search_student_by_phone():
    while True:
        # prompt the user to enter the phone number to search and validate input
        phone = input("\nEnter phone number: ").strip()
        if phone.isdigit():
            break  # valid input, exit the loop
        print("Invalid input. Phone number should contain numbers only.")  # error message for invalid input

    # ensure the 'phone' column is treated as a string and remove any extra spaces
    students["phone"] = students["phone"].astype(str).str.strip()

    # perform a case-insensitive search for the phone number in the 'phone' column
    result = students[students["phone"].str.contains(phone, na=False, case=False)]

    # check if any matches were found
    if result.empty:
        # no matching students found
        print(f"No student found with phone number: {phone}")
    else:
        # display the search results
        print(f"Search Results for Phone: {phone}")
        print(result)  # display the filtered DataFrame


# lists all courses taken by a student, identified by their last name
def courses_taken_by_student():
    while True:
        # prompt the user to enter the student's last name and validate input
        last_name = input("\nEnter student last name (letters only): ").strip()
        if last_name.isalpha():
            break  # valid input, exit the loop
        print("Invalid input. Last name should contain letters only.")  # error message for invalid input

    try:
        # ensure the 'id' and 'last_name' columns are treated as strings for consistent comparison
        grades["id"] = grades["id"].astype(str)
        grades["last_name"] = grades["last_name"].astype(str)

        # filter grades by the student's last name (case-insensitive)
        matching_students = grades[grades["last_name"].str.contains(last_name, case=False, na=False)]

        # check if no students match the last name
        if matching_students.empty:
            print(f"No students found with last name: {last_name}")
            return

        # if multiple students match, display the options
        if len(matching_students) > 1:
            print(f"Multiple students found with last name '{last_name}':")
            for i, row in matching_students.iterrows():
                print(f"[{i}] ID: {row['id']}, First Name: {row['first_name']}, Last Name: {row['last_name']}")

            # prompt the user to select a specific student
            try:
                selected_index = int(input("Enter the number corresponding to the correct student: ").strip())
                if selected_index not in matching_students.index:
                    print("Invalid selection. Please try again.")
                    return
            except ValueError:
                print("Invalid input. Please enter a number.")
                return

            # retrieve the selected student's data
            student_grades = matching_students.loc[[selected_index]]
        else:
            # only one student matches, select them directly
            student_grades = matching_students

        # collect courses with recorded grades (not "na")
        graded_courses = []
        for course in grades_headers[3:]:  # skip 'id', 'last_name', 'first_name'
            if student_grades[course].iloc[0] != "na":  # check if the course has a valid grade
                graded_courses.append(course)

        # check if no courses have grades
        if not graded_courses:
            print(f"No graded courses found for student with last name: {last_name}")
        else:
            # display the courses taken with grades
            print(f"Courses taken by {last_name}: {graded_courses}")
            return graded_courses  # return the list of courses with grades
    except Exception as e:
        # handle and display any errors that occur during the process
        print(f"An error occurred: {e}")


# lists all courses with grades for a specific student
def courses_with_grades_for_student():
    # prompt the user to enter the student's last name and validate input
    while True:
        last_name = input("\nEnter student last name: ").strip()
        if last_name.isalpha():
            break  # valid input, exit the loop
        print("invalid input. last name should contain letters only.")  # error message for invalid input

    try:
        # ensure the 'id' and 'last_name' columns are treated as strings for consistent comparison
        grades["id"] = grades["id"].astype(str)
        grades["last_name"] = grades["last_name"].astype(str)

        # filter grades by the student's last name (case-insensitive)
        matching_students = grades[grades["last_name"].str.contains(last_name, case=False, na=False)]

        # check if no students match the last name
        if matching_students.empty:
            print(f"no students found with last name: {last_name}")
            return

        # if multiple students match, display the options
        if len(matching_students) > 1:
            print(f"multiple students found with last name '{last_name}':")
            for i, (index, row) in enumerate(matching_students.iterrows()):
                print(f"[{i}] id: {row['id']}, first name: {row['first_name']}, last name: {row['last_name']}")

            # prompt the user to select a specific student
            try:
                selected_index = int(input("enter the number corresponding to the correct student: ").strip())
                if selected_index < 0 or selected_index >= len(matching_students):
                    print("invalid selection. please try again.")
                    return
            except ValueError:
                print("invalid input. please enter a number.")
                return

            # retrieve the selected student's data by their index
            student_grades = matching_students.iloc[[selected_index]]
        else:
            # only one student matches, select them directly
            student_grades = matching_students

        # collect courses with recorded grades (not "na") and their grades
        graded_courses = []
        for course in grades_headers[3:]:  # skip 'id', 'last_name', 'first_name'
            if course in student_grades.columns:  # ensure the column exists
                grade = student_grades[course].iloc[0]
                # include the course if the grade is a number and not "na"
                if isinstance(grade, (int, float)) or grade.isdigit():
                    graded_courses.append({"course": course, "grade": grade})

        # check if no courses have grades
        if not graded_courses:
            print(f"no graded courses found for student with last name: {last_name}")
        else:
            # display the courses taken and their grades
            print(f"courses taken by {last_name}:")
            for entry in graded_courses:
                print(f"{entry['course']}: {entry['grade']}")  # display course name and grade
            return graded_courses  # return the list of courses with grades
    except Exception as e:
        # handle and display any errors that occur during the process
        print(f"an error occurred: {e}")


# calculates the average grade for a specific student
def calculate_average_grade_for_student():
    # prompt the user to enter the student's last name and validate input
    while True:
        last_name = input("\nEnter student last name: ").strip()
        if last_name.isalpha():
            break  # valid input, exit the loop
        print("invalid input. last name should contain letters only.")  # error message for invalid input

    try:
        # ensure the 'id' and 'last_name' columns are treated as strings for consistent comparison
        grades["id"] = grades["id"].astype(str)
        grades["last_name"] = grades["last_name"].astype(str)

        # filter grades by the student's last name (case-insensitive)
        matching_students = grades[grades["last_name"].str.contains(last_name, case=False, na=False)]

        # check if no students match the last name
        if matching_students.empty:
            print(f"no students found with last name: {last_name}")
            return

        # if multiple students match, display the options
        if len(matching_students) > 1:
            print(f"multiple students found with last name '{last_name}':")
            for i, (index, row) in enumerate(matching_students.iterrows()):
                print(f"[{i}] id: {row['id']}, first name: {row['first_name']}, last name: {row['last_name']}")

            # prompt the user to select a specific student
            try:
                selected_index = int(input("enter the number corresponding to the correct student: ").strip())
                if selected_index < 0 or selected_index >= len(matching_students):
                    print("invalid selection. please try again.")
                    return
            except ValueError:
                print("invalid input. please enter a number.")
                return

            # retrieve the selected student's data by their index
            student_grades = matching_students.iloc[selected_index]
        else:
            # only one student matches, select them directly
            student_grades = matching_students.iloc[0]

        # collect numeric grades (ignore "na")
        numeric_grades = student_grades[3:].replace("na", pd.NA).dropna().astype(float)

        # check if no grades are available
        if numeric_grades.empty:
            print(f"no grades found for {student_grades['first_name']} {student_grades['last_name']}.")
        else:
            # calculate and display the mean grade
            mean_grade = numeric_grades.mean()
            print(f"average grade for {student_grades['first_name']} {student_grades['last_name']}: {mean_grade:.2f}")
            return mean_grade
    except Exception as e:
        # handle and display any errors that occur during the process
        print(f"an error occurred: {e}")


# calculates the average grade for a specific student in a specific term
def average_grade_for_student_in_term():
    while True:
        # prompt the user to enter the student's last name and validate input
        last_name = input("\nEnter student last name (letters only): ").strip()
        if last_name.isalpha():
            break  # valid input, exit the loop
        print("Invalid input. Last name should contain letters only.")  # error message for invalid input

    while True:
        # prompt the user to enter the term and validate input
        term = input("Enter term (Fall/Winter): ").strip().capitalize()
        if term in ["Fall", "Winter"]:
            break  # valid input, exit the loop
        print("Invalid input. Please enter 'Fall' or 'Winter'.")  # error message for invalid input

    try:
        # map the term to the appropriate postfix for grade column filtering
        term_postfix = "_F" if term == "Fall" else "_W"

        # ensure the 'id' and 'last_name' columns are treated as strings
        grades["id"] = grades["id"].astype(str)
        grades["last_name"] = grades["last_name"].astype(str)

        # filter students by last name (case-insensitive)
        matching_students = grades[grades["last_name"].str.contains(last_name, case=False, na=False)]

        # check if no students match the last name
        if matching_students.empty:
            print(f"No students found with last name: {last_name}")
            return

        # handle multiple students with the same last name
        if len(matching_students) > 1:
            print("\nMultiple students found with the same last name:")
            for i, row in matching_students.iterrows():
                print(f"{i + 1}. ID: {row['id']}, First Name: {row['first_name']}")

            # prompt the user to select a specific student
            while True:
                try:
                    choice = int(input(f"Enter the number of the student you're looking for (1-{len(matching_students)}): ").strip())
                    if 1 <= choice <= len(matching_students):
                        selected_student = matching_students.iloc[choice - 1]  # select the chosen student
                        break
                    else:
                        print(f"Invalid choice. Please select a number between 1 and {len(matching_students)}.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        else:
            # if only one student matches, select them directly
            selected_student = matching_students.iloc[0]

        # identify relevant columns for the specified term
        term_columns = [col for col in grades.columns if col.endswith(term_postfix)]

        # filter grades for the selected student and term columns
        student_grades = grades.loc[grades["id"] == selected_student["id"], term_columns]

        # convert grades to numeric, ignoring invalid entries (e.g., "na")
        student_grades = student_grades.apply(pd.to_numeric, errors="coerce")

        # calculate the mean grade across relevant term columns
        avg_grade = student_grades.mean(axis=1).iloc[0]

        # display the result if valid grades exist
        if pd.notna(avg_grade):
            print(f"Average Grade for {selected_student['first_name']} {selected_student['last_name']} in {term}: {avg_grade:.2f}")
        else:
            print(f"No valid grades found for {selected_student['first_name']} {selected_student['last_name']} in {term}.")
    except Exception as e:
        # handle and display any errors that occur during the process
        print(f"An error occurred: {e}")

# calculates the average grade for a specific course by name
def average_grade_for_course():
    # prompt the user to enter the course name
    course_name = input("\nEnter course name: ").strip()

    try:
        # filter the courses dataframe to find matching course names (case-insensitive)
        matching_courses = courses[courses["name"].str.contains(course_name, case=False, na=False)]

        # check if no courses match the entered name
        if matching_courses.empty:
            print(f"No courses found with name: {course_name}")
            return

        # display matching courses and ask the user to select one
        print("\nMatching courses:")
        for i, row in matching_courses.iterrows():
            print(f"[{i + 1}] {row['name']} - Semester: {row['semester']} (Code: {row['code']})")

        while True:
            # prompt the user to select a specific course
            try:
                choice = int(input(f"Enter the number of the course you want to select (1-{len(matching_courses)}): ").strip())
                if 1 <= choice <= len(matching_courses):
                    selected_course = matching_courses.iloc[choice - 1]  # select the chosen course
                    break
                else:
                    print(f"Invalid choice. Please select a number between 1 and {len(matching_courses)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # determine the grade column in the grades dataframe
        course_column = f"{selected_course['name']}_{selected_course['semester'][0].upper()}"  # format e.g., CS2020_F for Fall

        # check if the course column exists in the grades dataframe
        if course_column not in grades.columns:
            print(f"No grades recorded for course: {selected_course['name']} (Semester: {selected_course['semester']}).")
            return

        # extract grades for the selected course and convert them to numeric
        course_grades = grades[course_column].apply(pd.to_numeric, errors="coerce")

        # filter out invalid or missing grades
        valid_grades = course_grades.dropna()

        # check if no valid grades are available for the course
        if valid_grades.empty:
            print(f"No valid grades found for course: {selected_course['name']} (Semester: {selected_course['semester']}).")
        else:
            # calculate the mean grade
            avg_grade = valid_grades.mean()

            # display the result
            print(f"Average grade for {selected_course['name']} (Semester: {selected_course['semester']}): {avg_grade:.2f}")
    except Exception as e:
        # handle and display any errors that occur during the process
        print(f"An error occurred: {e}")


# clears the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')  # uses 'cls' for windows and 'clear' for unix-based systems

# main function that serves as the entry point for the program
def main():
    
    # displays the menu options for the user
    def menu():
        print("""
        Menu:
        1. Output all students
        2. Sort students by name (alphabetically)
        3. Output all courses
        4. Courses by semester
        5. Courses by semester (sorted by name)
        6. Add new (student, cousre, grade)
        7. Update student info
        8. Search course by name 
        9. Search course by code 
        10. Search student by last name 
        11. Search student by phone number
        12. Courses taken by a student
        13. Courses with grades for a student
        14. Average grade for a student
        15. Average grade for a student in a specific term
        16. Average grade for a course
        0. Exit
        """)

    while True:
        menu()  # displays the menu
        choice = input("Enter your choice: ").strip()  # gets the user's choice

        if choice == "0":
            print("Exiting the program. Goodbye!")  # exits the program
            break
        elif choice == "1":
            output_stduents()  # outputs all students
        elif choice == "2":
            sort_student()  # sorts students by name
        elif choice == "3":
            output_course()  # outputs all courses
        elif choice == "4":
            course_by_semester()  # outputs courses for a specific semester
        elif choice == "5":
            course_by_semester_sorted()  # outputs courses for a specific semester sorted by name
        elif choice == "6":
            get_user_action()  # adds a new student
        elif choice == "7":
            update_student_info()  # updates student information
        elif choice == "8":
            search_course_by_name()  # searches for a student by last name
        elif choice == "9":
            search_course_by_code()  # searches for a student by phone number
        elif choice == "10":
            search_student_by_last_name()  # searches for a course by name
        elif choice == "11":
            search_student_by_phone()  # searches for a course by code
        elif choice == "12":
            courses_taken_by_student()  # lists courses taken by a student
        elif choice == "13":
            courses_with_grades_for_student()  # lists courses with grades for a student
        elif choice == "14":
            calculate_average_grade_for_student()  # calculates the average grade for a student
        elif choice == "15":
            average_grade_for_student_in_term()  # calculates the average grade for a student in a specific term
        elif choice == "16":
            average_grade_for_course()  # calculates the average grade for a course
        else:
            print("Invalid choice. Please try again.")  # message for invalid menu choice

        input("\nPress any key to contine")
        clear_screen()


# ensures the script runs only when executed directly, not when imported
if __name__ == "__main__":
    main()

