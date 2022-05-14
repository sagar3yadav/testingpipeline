import os
from datetime import datetime

path = '/root/git/testpipeline/testingpipeline'

data = "testdata writing in a text file like log file"

print(data)
# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y-%H:%M")
print("date and time =", dt_string)

# Specify the file name

prefile = "logs-"
current_date_and_time_string = str(dt_string)
extension = ".txt"

file = prefile +  current_date_and_time_string + extension


# Before creating
dir_list = os.listdir(path) 
print("List of directories and files before creation:")
print(dir_list)
print()
  
# Creating a file at specified location
with open(os.path.join(path, file), 'w') as fp:
    pass
    # To write data to new file uncomment
    # this fp.write("New file created")
  
# After creating 
dir_list = os.listdir(path)
print("List of directories and files after creation:")
print(dir_list)
