# import module
from datetime import datetime

data = "hello sagar everthing is working fine in this\n Congratulation !!!!! \n You have completed your assignment\n"

# get current date and time
current_datetime = datetime.now()

# convert datetime obj to string
str_current_datetime = str(current_datetime)

# create a file object along with extension
file_name = "logs-"+str_current_datetime+".txt"
file = open(file_name, 'w')
file.writelines(data)  
file.close()
