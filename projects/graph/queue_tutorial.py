# first in first out
# last in first out
# priority

import queue

q = queue.Queue()

q.put(5) # put an item in 

print(q.get()) # get an item out

print(q.empty())  # so queue is empty

# first in first out
for i in range(5):
    q.put(i)

# one thread putting item into queue and another thread pulling out our items
while not q.empty(): # with q.get, our program will freeze before q.get is empty
    print(q.get(), end= '   ')