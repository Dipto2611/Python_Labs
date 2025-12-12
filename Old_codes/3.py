'''Write a Python program to create a dictionary of 5 students with their marks.
Add one more student to the dictionary and display all key value pairs.'''

students = {'Dipto': 85, 'Kavya': 90, 'Jeeps': 78, 'Abhigyan': 88, 'Arjun': 92}
students['Nayan'] = 80

# for name, marks in students.items():
#     print(name, ":", marks)


for i in students:
    print(i,":",students[i])