n = int(input().strip())
string = input().strip()

def adrian_ans(string):
    ad_string = 'ABC'
    correct=0
    for i in range(len(string)):
        if string[i]==ad_string[i%3]:
            correct+=1
    return correct

def bruno_ans(string):
    br_string = "BABC"
    correct=0
    for i in range(len(string)):
        if string[i]==br_string[i%4]:
            correct+=1
    return correct

def goran_ans(string):
    go_string = "CCAABB"
    correct=0
    for i in range(len(string)):
        if string[i]==go_string[i%6]:
            correct+=1
    return correct

def print_results(ad_cor,br_cor,go_cor):
    maxScore = max([ad_cor,br_cor,go_cor])
    print(maxScore)
    if ad_cor==maxScore:
        print("Adrian")
    if br_cor==maxScore:
        print("Bruno")
    if go_cor==maxScore:
        print("Goran")

ad_cor = adrian_ans(string)
br_cor = bruno_ans(string)
go_cor = goran_ans(string)

print_results(ad_cor,br_cor,go_cor)
