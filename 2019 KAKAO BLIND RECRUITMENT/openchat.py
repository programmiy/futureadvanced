import sys
result=[]
record = sys.stdin.read().strip().split(" ")
separator = ' '  # You can choose any separator you want, e.g., ', ', '-' or ''
result_string = separator.join(record)
record = result_string

def solution(result):
    
    
    
            
    answer = result
    print(*answer)
    return answer
solution(record)