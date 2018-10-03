string = input().strip()
chars = []
for i in string:
    if ord(i) == ord("_"):
        chars.append(0)
    elif i.isupper():
        chars.append(1)
    elif i.islower():
        chars.append(2)
    else:
        chars.append(3)
whitespace = chars.count(0)
lowercase = chars.count(2)
uppercase = chars.count(1)
symbols = chars.count(3)
print("{:0.12f}".format(whitespace/len(chars)))
print("{:0.12f}".format(lowercase/len(chars)))
print("{:0.12f}".format(uppercase/len(chars)))
print("{:0.12f}".format(symbols/len(chars)))
