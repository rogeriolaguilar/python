file = open("test.txt", 'wt')
for i in range(20 * 1000):    
    file.write("Line number {}\n".format(i))
file.close()

