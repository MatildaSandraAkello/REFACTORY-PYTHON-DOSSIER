#A function defining student details
def capture_student_details(Name, Age, Gender, Program, Year_of_study, Test1, Test2, Coursework, Final_mark):

    #A dictionary to store student's details
    student = {"Name": Name,
               "Age":Age,
               "Gender":Gender,
               "Program":Program,
               "Year_of_study":Year_of_study,
               "Test1":Test1,
               "Test2":Test2,
               "Coursework":Coursework,
               "Final_exam":Final_mark}
    
    #Acessing our marks from the dictionary , student
    marks = [student["Test1"], student["Test2"], student["Coursework"]]
    
    # Sorting our marks to get the two top marks in descending order
    best_two_marks = sorted(marks ,reverse=False)[2]
    
    #Calculating our average score for out of 40%
    average_tests = (sum(best_two_marks) / 2)* 0.4

    #Calculating our final mark out of 60%
    final_exam_mark = student["Final_exam"]* 0.6

    #Calculating our total marks out of 100%
    total_marks = average_tests + final_exam_mark
    
    #Adding the final marks to our dictionary
    student.update({"actual_mark":total_marks})
    
    return student

#Invoking our function

print(capture_student_details('Matilda', 25, 'Female', 'Python', "2025", 65, 82, 75, 55))