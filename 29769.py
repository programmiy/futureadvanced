
days = int(input())
day = 0

skills = list(map(int, input().split()))


Q = int(input())


changes = []
for _ in range(Q):
    x, y = map(int, input().split())
    changes.append([x, y])


def full_control(skills):
    
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
                    
                    break
                elif cnt == 0:
                    cnt = index 
                    
                    break
                
                break
            elif data == i:
                
                    
                cnt +=1
                index +=1
        
    return data, cnt
    
        
        
for i in changes:
    member = i[0]
    ootd = i[1]
    
    skills[member-1] = ootd
    
    data, cnt = full_control(skills)
    print(data, "", cnt)
    

