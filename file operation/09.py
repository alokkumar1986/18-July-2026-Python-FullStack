import os

if os.path.exists("demo/demo.txt"):
    os.remove("demo/demo.txt")
if os.path.exists('demo'):
    os.rmdir('demo')