# Faster way to read files
file = open("test.txt", 'rt')
for line in file:
    print(line)
file.close()
