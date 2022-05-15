import platform
import os
import psutil
from datetime import datetime
from datetime import date, timedelta
my_system = platform.uname()

print(f"System: {my_system.system}")
print(f"Node Name: {my_system.node}")
print(f"Release: {my_system.release}")
print(f"Version: {my_system.version}")
print(f"Machine: {my_system.machine}")
print(f"Processor: {my_system.processor}")

Actualdate = date.today().strftime("%m-%d-%y")

globallist = []

#def main():
#print('*** Create a list of all running processes ***')
listOfProcessNames = list()

    # Iterate over all running processes

for proc in psutil.process_iter():

       # Get process detail as dictionary

    pInfoDict = proc.as_dict(attrs=['pid', 'name', 'cpu_percent'])

       # Append dict of process detail in list

    listOfProcessNames.append(pInfoDict)

    # Iterate over the list of dictionary and print each elem

for elem in listOfProcessNames:

       # print("elem")

    globallist.append(elem)
    
print("ALL RUNNING PROCESS ON THE OS -------------------------")
print(globallist)

print("WRITING LOGS INTO THE TXT FILE")
# Writng logs into a file----------------------
current_datetime = datetime.now()
# convert datetime obj to string
str_current_datetime = str(current_datetime)
# create a file object along with extension
file_name = "logs-"+str_current_datetime+".txt"
file = open(file_name, 'w')
file.writelines(str(globallist))
file.close()

print("LOGS HAS BEEN GENTERATED AND STORED IN THIS FILE :" + file_name)
