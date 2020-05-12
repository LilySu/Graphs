from util import Stack, Queue 

q = Queue() # first in first out

for i in range(5):
    q.enqueue(i)

for i in range(5):
    print(q.dequeue())
    print('Queue size: ' + str(q.size()))

s = Stack()

for i in range(5):
    s.push(i)

for i in range(5):
    print(s.pop())
    print('stack size: ' + str(s.size()))