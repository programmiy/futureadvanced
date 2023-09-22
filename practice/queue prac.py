
from queue import Queue

q = Queue()

q.put(123)
print(q.get())
q.put(456)
print(q.get())