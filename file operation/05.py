try: 
    f = open('demo.txt', 'a')
except FileNotFoundError:
    print("File not found")
else: 
    f.write("10.This is a demo file.")
    f.close()