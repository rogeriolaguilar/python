# Write a function \color{red}{\verb|count_letters(word_list)|}count_letters(word_list) that 
# takes as input a list of words that are composed entirely of lower case letters . This 
# function should return the lower case letter that appears most frequently (total number of 
# occurrences) in the words in \color{red}{\verb|word_list|}word_list. (In the case of ties, 
# return the earliest letter in alphabetical order.)

# The Python code snippet below represents a start at implementing \color{red}{\verb|
# count_letters|}count_letters using a dictionary \color{red}{\verb|letter_count|}letter_count 
# whose keys are the lower case letters and whose values are the corresponding number of 
# occurrences of each letter in the strings in \color{red}{\verb|word_list|}word_list.


def count_letters(word_list):
    """ See question description """
    
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    letter_count = {}
    for letter in ALPHABET:
        letter_count[letter] = 0
    
    # enter code here
    for word in word_list:
        for letter in word:
            letter_count[letter] += 1
  
    result = None
    maximum = 0
    for letter, count in letter_count.items():
        if count > maximum :
            maximum = count 
            result = letter
    return result

result = count_letters(["hello","world"])
print(result) # l

result = count_letters(["test","letter"])
print(result) # t

result = count_letters(["bcd","bcd"])
print(result) # b


monty_quote = "listen strange women lying in ponds distributing swords is no basis for a system of government supreme executive power derives from a mandate from the masses not from some farcical aquatic ceremony"

monty_words = monty_quote.split(" ")
result = count_letters(monty_words)
print(result)
