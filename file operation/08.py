import os

if not os.path.exists('demo'):
    os.mkdir('demo')
if not os.path.exists('demo/demo.txt'):
    f = open('demo/demo.txt', 'x')
    f.close()

