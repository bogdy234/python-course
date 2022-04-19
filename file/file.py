# file = open('data.txt', 'r+')

# r -> only read, not write, is default to open function (no second param needed)
# w -> write access
# a -> appending access, write, existing data remains
# r+ -> read + write

# file.write('Hello2')
# file.close()

# with open('data.txt', 'w') as file:
#     file.write('python course\n')
#     file.write('python course2\n')

# with open('data.txt', 'r') as file:
#     for line in file.readlines():
#         print(line, 'line')

# with open('data.txt', 'r') as file:
#     for line in list(file):
#         print(line)

with open('data.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        print(line)
