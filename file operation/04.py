try:
    f = open('demo.txt', 'r')
except FileNotFoundError:
    print("File not found")
else: 
    content = f.read()
    print(content)
    f.close()
   