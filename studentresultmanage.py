# Students = {1:{"Name": "Mehak","Marks":98},
#            2:{"Name": "Rishita","Marks":95},
#            3:{"Name": "Payal","Marks":79},
#            4:{"Name": "Kanika","Marks":80},
#            5:{"Name" : "Saru","Marks":67}}

# marks_list = list(Students.values())
# #marks_list = [student["Marks"] for student in Students.values()]

# average = sum(marks_list)/len(marks_list)
# print("Average marks : ", average)

# highest_marks = max(marks_list)
# for name , marks in Students.items():
#     if marks == highest_marks:
#         print("Topper is :",name)
#         print("Topper marks :",marks)

# for name ,marks in Students.items():
#   if marks >= 90:
#     grade = "A+" 
#   elif marks >=80:
#     Grade = "A" 
#   elif marks >=70:
#     Grade = "B"
#   elif marks >=60:
#     Grade = "C" 
#   else:
#     print("Fail")

#     print(name,"-",marks,"Grade",Grade)

    

    

Students = {
    1: {"Name": "Mehak", "Marks": 98},
    2: {"Name": "Rishita", "Marks": 95},
    3: {"Name": "Payal", "Marks": 79},
    4: {"Name": "Kanika", "Marks": 80},
    5: {"Name": "Saru", "Marks": 67}
}

# Average
marks_list = [student["Marks"] for student in Students.values()]

average = sum(marks_list) / len(marks_list)
print("Average marks:", average)

# Topper
highest_marks = max(marks_list)

for roll, student in Students.items():
    if student["Marks"] == highest_marks:
        print("Topper is:", student["Name"])
        print("Topper marks:", student["Marks"])

# Grades
for roll, student in Students.items():

    marks = student["Marks"]

    if marks >= 90:
        grade = "A+"

    elif marks >= 80:
        grade = "A"

    elif marks >= 70:
        grade = "B"

    elif marks >= 60:
        grade = "C"

    else:
        grade = "Fail"

    print(student["Name"], "-", marks, "Grade:", grade)