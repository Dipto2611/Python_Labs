#create and add one value:

students = {'Dipto': 85, 'Kavya': 90, 'Jeeps': 78, 'Abhigyan': 88, 'Arjun': 92}
students['Nayan'] = 80

for i in students:
    print(i,":",students[i])

print()

print("Item method provided below:")

for i,j in students.items():
    print(i,"=>",j)