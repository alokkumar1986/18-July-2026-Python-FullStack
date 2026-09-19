#write a program to read only 5th line of the file
# f = open('demo.txt', 'r')
# content = f.readlines()
# print(content[4])           
# f.close()

with open('demo.txt', 'r') as f:
    content = f.readlines()
    print(content[4])   