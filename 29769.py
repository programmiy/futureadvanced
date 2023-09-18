
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
def full_control(skills, len_skills):
    print("Full Control")
    data = None
    cnt = 1
    index = 1
    cv = 1
    for i in skills:
        if data == None:
            data = i
            index +=1
        else:
            if data < i:
                data = i
                cv = 1
                if cnt != index and cv >1:
                    index = 1
                    print(cv, "cv")
                    print(index, "index")
                    print(cnt, "cnt")
                elif cnt != index and cv==1:
                    index = cnt
                    print(cv, "cv")
                    print(index, "index")
                    print(cnt, "cnt")   
                else:
                    
                    index+=1   
                    cnt = index 
                    print(index, "index")
                    print(cnt, "cnt")
                    
            elif data > i:
                
                if cnt > 1 and cv ==1:
                    cnt = index 
                    print(index, "index")
                    print(cnt, "cnt")
                    break
                elif cnt == 0:
                    cnt = index 
                    print(index, "index")
                    print(cnt, "cnt")
                    break
                elif cnt ==1:
                    index =cnt 
                    print(index, "index")
                    print(cnt, "cnt")
                    break
                elif cv >1 and cnt>1:
                    index = 1
                    print(cv, "cv")
                    print(index, "index")
                    print(cnt, "cnt")
            elif data == i:
                
                
                if len_skills == cnt:
                    if cnt != index and cv >1 and cnt>1:
                        index = 1
                        print(cv, "cv")
                        print(index, "index")
                        print(cnt, "cnt")
                    elif cnt != index and cv==1 and cnt>1:
                        index = cnt
                        print(cv, "cv")
                        print(index, "index")
                        print(cnt, "cnt")   
                    else:
                        if cnt ==1:
                            index = cnt
                            print("조기종결")
                        else:
                            index+=1   
                            cnt = index 
                            print(index, "index")
                            print(cnt, "cnt")
                cv +=1    
                cnt +=1
        print("data =", data, "cnt =", cnt)
    if cv ==len_skills and cnt==len_skills:
            index = 1
    print("리턴 전 값", index, cnt)
    return index, cnt
    
        
        
for i in changes:
    member = i[0]
    ootd = i[1]
    print(member, "+", ootd)
    skills[member-1] = ootd
    print(skills)
    len_skills= len(skills)
    print("최종 출력")
    data, cnt = full_control(skills, len_skills)
    print(data, "", cnt)
    print(" ***********************************")

