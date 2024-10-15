# Colter Makowski
# UWYO COSC 1010
# 10/15/24
# HW 01
# Lab Section:15
# Sources, people worked with, help given to:
# your
# comments
# here
# Homework Question:
#
# You are given a list of dictionaries where each dictionary represents a student
# and their scores
# in different subjects.
#
# Student Data:
students = [
{"name": "Alice", "scores": {"Math": 85, "Science": 90, "English": 78}},
{"name": "Bob", "scores": {"Math": 70, "Science": 88, "English": 82}},
{"name": "Charlie", "scores": {"Math": 92, "Science": 81, "English": 89}},
{"name": "David", "scores": {"Math": 60, "Science": 75, "English": 80}}
]
new_dictionary = {}
for student in students:
    name = student["name"]
    scores = student["scores"].values ()
    avg_scores = sum(scores)/len(scores)
    print(f"{student["name"]} scored on average {avg_scores}")
    new_dictionary[name] = avg_scores  # Store average score in dictionary

# Print the names of students whose average score is greater than 80
print("Students with average score greater than 80:")
for name, avg_score in new_dictionary.items():
    if avg_score > 80:
        print(name)

#Write a Python program that:
# 1. Calculates the average score for each student.
# 2. Stores these averages in a new dictionary where the student’s name is the key
# and their average score is the value.
# 3. Prints the names of students whose average score is greater than 80.
# Your task is to calculate the average scores for each student and print the names
#of students
# whose average score is greater than 80.
#Solution

