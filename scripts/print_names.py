"""
This python files reads the data from 'name.txt'
and print the data present on line.
"""
f=open("name.txt")
data=f.readlines()
for line in data:
    print(line)
f.close()
