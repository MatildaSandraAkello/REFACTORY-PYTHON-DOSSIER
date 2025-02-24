# MAPPING DATA TYPE
# Dictinaries - hold key:value pairs thus can stored more information for example about a student in one memory space
# You can manipulate dictionary ie mutable e.g append, delete

student_details = {"name":'Matilda', 'track':"Python", 'Gender':'Female', "Age":26}
student_details['name']
student_details.keys()
student_details.values()

# SETS - {} they are unordered and don't repeat values hence don't have defined Index positions
# You can manipulate sets ie mutable e.g append, delete
# Can't be accessed by the index position

student_id = {123,245,284,123,65,10}
print(student_id)
student_id.add(12)
student_id
