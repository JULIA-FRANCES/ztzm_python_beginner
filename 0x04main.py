# Exercise 5 Solution - Build a Simple Student Database

# Initial database setup with 3 students and their courses (stored as a list)
student_db = {
    "Alice": ["Calculus", "Data Science", "Chemistry"],
    "Bob": ["Web Development", "Graphic Design", "Machine Language"],
    "Charlie": ["Cybersecurity", "Networking", "Math"]
}

# Task 1: Add a new course to an existing student 
student_db["Alice"].append("Machine Learning")

#  Task 2: Remove a course from another student 
student_db["Bob"].remove("Graphic Design")

#  Task 3: Print out all students and their courses nicely formatted 
for name, courses in student_db.items():
    print(f"Student: {name}")
    print("Courses:", ", ".join(courses))
    print("---")