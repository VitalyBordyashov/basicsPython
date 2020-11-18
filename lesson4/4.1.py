from sys import argv
def my_fanc(a, b, c):
    return (a * b) + c
file_path, a, b, c = argv
print(my_fanc(int(a), int(b), int(c)))