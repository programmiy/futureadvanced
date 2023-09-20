letter = input()
cnt = 0
index = 0

while index < len(letter):
    if letter[index:index+4] == "DKSH":
        cnt += 1
        index += 4
    else:
        index += 1
#chatgpat도움받음 100%
print(cnt)