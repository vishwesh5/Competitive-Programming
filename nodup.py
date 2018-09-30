sentence = input().strip().split()
words = set(sentence)
flag=True
for i in words:
    if sentence.count(i) > 1:
        flag=False
        print("no")
        break
if flag:
    print("yes")
