import os

if os.path.exists("demo"):
    for filename in os.listdir("demo"):
        os.remove(f"demo/{filename}")
    os.rmdir("demo")