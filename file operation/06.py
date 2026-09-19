try: 
    f = open('demo.txt', 'w')
except FileNotFoundError:
    print("File not found")
else: 
    f.write("11.This is a demo file.")
    f.close()