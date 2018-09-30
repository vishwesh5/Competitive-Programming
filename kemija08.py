encoded_str = input().strip().split()
decoded = []
vowels = ['a','e','i','o','u']
for word in encoded_str:
    decoded_str=''
    i=0
    while i < len(word):
        #print(decoded_str,word[i])
        if word[i] in vowels:
            decoded_str += word[i]
            i+=3
        else:
            decoded_str += word[i]
            i+=1
    decoded.append(decoded_str)
print(' '.join(decoded))
