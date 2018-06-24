
# Formatting strings
print("The capital of {} is {}".format("Italia", "Roma"))

print("What is the capital of {0}? The capital of {0} is {1}".format("Italia", "Roma"))

print("{0:>7} {1:^3}".format("May", "5"))
print("{0:>7} {1:^3}".format("June", "21"))


num = 3.283663293
output = "{0:>10.3f} {0:.2f}".format(num)
print(output)


def count_vowels(string):
    return string.count('a') + string.count('e') + string.count('i') + string.count('o') + string.count('u')
print(count_vowels("aaassseefffgggiiijjjoOOkkkuuuu"))
print(count_vowels("aovvouOucvicIIOveeOIclOeuvvauouuvciOIsle"))


def demystify(string):
    return string.replace('l', 'a').replace('1', 'b')
print(demystify("lll111l1l1l1111lll"))
print(demystify("111l1l11l11lll1lll1lll11111ll11l1ll1l111"))

