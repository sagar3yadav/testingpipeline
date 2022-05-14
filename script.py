import platform
import os
from datetime import date, timedelta
my_system = platform.uname()
 
print(f"System: {my_system.system}")
print(f"Node Name: {my_system.node}")
print(f"Release: {my_system.release}")
print(f"Version: {my_system.version}")
print(f"Machine: {my_system.machine}")
print(f"Processor: {my_system.processor}")



Actualdate = date.today().strftime("%m-%d-%y")
print(Actualdate)
