import os

pwd = os.getcwd()
print("Current directory: ", pwd)

py_files = [f for f in os.listdir('.') if f.endswith('.py')]
print("Python source files:", py_files)