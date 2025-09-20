str1 = "hello"
str2 = "world"
result = str1 + " " + str2
print(result)

#length of string

text = "Python is awesome"
length = len(text)
print("Length of the string:" , length)

# lower uppper case
text = "Python is awesome"
uppercase = text.upper()
lowercase = text.lower()
print("Uppercase:" , uppercase)
print("lowercase" , lowercase)

# replace

text = "Python is awesome"
new_text = text.replace("awesome", "great")
print("replaced text:", new_text)


# split

text = "Python is awesome"
words = text.split()
print("words:", words)
#
#
#

#strip
text = "    Some spaces around    "
stripped_text = text.strip()
print("stripped text:", stripped_text)

#
#
#
#substring

text = "Python is awesome"
substring = "is"
if substring in text:
    print(substring, "found in the text")




