#ASSIGNMENT
"""
A Python Function that stores student details to include;
1. Name of Student
2. Age
3. Gender
4. Program
5. School/Faculty
6. Year of study
7. Date of Birth (DOB)
8. Test 1 marks (out of 40%)
9. Test 2 marks (out of 40%)
10. Final Exam Marks (out of 60%)
11. Actual Marks (out of 100%)
"""


def student_details():
    print("Enter your details") #this is to prepare users mentally to start entering their data
    dict = {'Name':input("Name: "),
            'Age':input("Age: "),
            'Gender':input('Gender: '),
            'Program':input("Program: "),
            'School/Faculty':input('School/Faculty: '),
            'Year_of_study':input("Year of study: "),
            'DOB':input('DOB: '),
            'Test1_marks':int(input("Test1 marks: ")),
            'Test2_marks':int(input('Test2 marks: ')),
            'Final_exam':int(input('Final exam marks: ')), 
            }
           
    mark1 = 0.4 * ((dict["Test1_marks"] + dict["Test2_marks"])/2) #Average of test1 & test2 marks marked out of 40%
    mark2 = 0.6 * dict["Final_exam"] #Final exam marked out of 60%
    actual_marks = int(mark1 + mark2) #Actual mark at 100%
    dict.update({'Actual marks ': actual_marks}) #add our actual marks back to the dictionary
    return dict
    
print(student_details())

"""
New Assignment (3rd/3/2025)
using dynamic functions together with input function,
create a program that can capture a student's details- one at a time
name,age,gender, program, year of study
first test mark
2nd test mark
coursework mark
final mark
calculate the 2 best done average (marked out of 40%)
Exam mark is marked out of 60%

"""

