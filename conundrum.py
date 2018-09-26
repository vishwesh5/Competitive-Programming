cipher_text = input().strip()
name="PER"
count=0
for i in range(len(cipher_text)):
    if cipher_text[i] != name[i%3]:
        count+=1
print(count)
