import sys
result=[]
record = sys.stdin.read().strip().split(" ")
separator = ' '  # You can choose any separator you want, e.g., ', ', '-' or ''
result_string = separator.join(record)
record = result_string

def solution(result):
    """
    This function takes a result as input and returns it after printing.
    
    Args:
        result (list): The result to be printed.
    
    Returns:
        list: The input result.
    """
    answer = result
    print(*answer)
    return answer
solution(record)