# Exercise 1: Simple Student Database

students = {
    "Alice": ["Math", "English", "Biology"],
    "Bob": ["History", "Physics"],
    "Charlie": ["Art", "Economics", "Math"]
}

# Task 1: Add a new course to Alice
students["Alice"].append("Computer Science")

# Task 2: Remove 'Art' from Charlie's courses
students["Charlie"].remove("Art")

# Task 3: Print all student names and their courses
for name, courses in students.items():
    print(f"Student: {name}")
    print("Courses:", ", ".join(courses))
    print("---")