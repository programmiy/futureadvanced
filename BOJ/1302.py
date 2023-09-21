
books = dict()

for _ in range(int(input())):
    
    title = input()
    if title in books:
        books[title] += 1
    else:
        books[title] = 1
    
bestseller = max(books.values())    
arr = []

for key, value in books.items():
    if value == bestseller:
        arr.append(key) # 리스트로 최적화? >>> 같은 판매량을 가진 책이 여러개 있을 가능성. 책참고
        
        
arr.sort()
print(arr[0])