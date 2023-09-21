import sys

company = set()
for _ in range(int(sys.stdin.readline())):
    name, exist = sys.stdin.readline().split()
    if exist == 'enter':
        company.add(name)
    elif exist == 'leave' and name:
        company.remove(name)
    
 
for i in sorted(company, reverse=True):
    print(i)

    