from sys import argv
def my_fanc(a, b):
    return a / b
file_path, a, b = argv
print(my_fanc(int(a), int(b)))