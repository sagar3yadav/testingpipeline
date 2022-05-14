from datetime import datetime

data = "testdata writing in a text file like log file"

print(data)
# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y-%H:%M:%S")
print("date and time =", dt_string)	


#str_dictionary = repr(data)
#file.write("a_dictionary = " + str_dictionary )


prefile = "logs-"
current_date_and_time_string = str(dt_string)
extension = ".txt"

file_name = prefile +  current_date_and_time_string + extension
file = open(file_name, 'w')
file.close()
#outname = mainfile.replace("pythonscript_logs" + dt_string + ".txt")
