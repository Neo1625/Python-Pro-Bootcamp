import random
#numbers = [1, 2, 3]
#new_numbers = [item+1 for item in numbers]
#print(new_numbers)

#name = "Angela"
#new_list = [letter for letter in name]
#print(new_list)

#numbers = [n*2 for n in range(1, 5)]
#print(numbers)

#names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
#short_names = [name for name in names if len(name) < 5]
#print(short_names)

#upper_case_names = [name.upper() for name in names if len(name) > 5]
#print(upper_case_names)

#student_scores = {student:random.randint(1, 100) for student in names}

#passed_students = {student:score for (student, score) in student_scores.items() if score >=50}
#print(passed_students)
import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score" : [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
#print(student_data_frame.to_csv)
#Loop through a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.student)