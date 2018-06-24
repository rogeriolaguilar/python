print("_AAA_" * 4)

print("Number: " + str(4.0)) # Number: 4
print("Number: " + str(4)) # Number: 

phrase = "This is a phrase."
print(phrase[0]) # T
print(phrase[1]) # h
print(len(phrase)) # 17
print(phrase[-1]) # .
print("len -1", phrase[len(phrase) - 1]) # .
print("Phrase 1:3", phrase[1:3])
print("Phrase 1:", phrase[1:])

# find first ocurrence of string
print("find first 'is' position: ", phrase.find("is")) # 2
print("find last 'is' position: ", phrase.rfind("is")) # 1
print("find 'is': ", phrase.find(" is ")) # 1
print("Starts with 'This': ", phrase.startswith("This")) # true
