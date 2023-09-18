
days = int(input())
day = 0

skills = list(map(int, input().split()))


Q = int(input())


changes = []
for _ in range(Q):
    x, y = map(int, input().split())
    changes.append([x, y])

# 입력된 정보를 출력해보겠습니다.
print("N:", days)
print("A:", skills)
print("Q:", Q)
print("Changes:", changes)
a = skills

print("start")
def full_control(skills):
    print("Full Control")
    data = None
    cnt = 1
    index = 0
    for i in skills:
        if data == None:
            data = i
            index +=1
        else:
            if data < i:
                data = i
                cnt = 0
                    
            elif data > i:
                
                if cnt >= 1:
                    cnt = index 
                    print(index, "index")
                    print(cnt, "cnt")
                    break
                elif cnt == 0:
                    cnt = index 
                    print(index, "index")
                    print(cnt, "cnt")
                    break
                
                break
            elif data == i:
                
                    
                cnt +=1
                index +=1
        print("data =", data, "cnt =", cnt)    
    print("리턴 전 값", data, cnt)
    return data, cnt
    
        
        
for i in changes:
    member = i[0]
    ootd = i[1]
    print(member, "+", ootd)
    skills[member-1] = ootd
    print(skills)
    print("최종 출력")
    data, cnt = full_control(skills)
    print(data, "", cnt)
    print(" ***********************************")
skills = a
