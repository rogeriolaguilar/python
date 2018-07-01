# Modes for wrinting
# w - write
# a - write appending to the end of file
# t - text (default)
# b - binary
# + - open for read and write

# slow way to read large files
file = open("test.txt", "rt")
for line in file.readlines():
    print(line)
file.close()
