# f = open('demo.txt', 'r')
# content = f.read()
# print(content)
# f.close()
#===========================================

# with open('demo.txt', 'r') as f:
#     content = f.read()
#     print(content)

#===========================================

# f = open('demo.txt', 'r')
# content = f.readlines()
# print(content)
# f.close()


#===========================================

# with open('demo.txt', 'r') as f:
#     content = f.readlines()
#     print(content)


#===========================================

# f = open('demo.txt', 'r')
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()

with open('demo.txt', 'r') as f:
    print(f.readline())
    print(f.readline())
    print(f.readline()) 

