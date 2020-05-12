# def fibonacci(n):
#     if n ==1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         # sum of previous functions
#         return fibonacci(n-1) + fibonacci(n-2)

# for n in range(1, 30):
#     print(n, ':', fibonacci(n))


# # Memoization  - cache
# # Store values for recent function calls so future values don't have to repeat the work

# fibonacci_cache = {} # store recent function calls

# def fibonacci(n):
#     # If we have cached the value, then return it
#     if n in fibonacci_cache:
#         return fibonacci_cache[n]

#     # If value is not cached,
#     # Compute the Nth term, cache it, then return it
#     if n == 1:
#         value = 1
#     elif n == 2:
#         value = 1
#     elif n > 2:
#         value = fibonacci(n-1) + fibonacci(n-2)

#     # Store in cache dictionary, then return
#     fibonacci_cache[n] = value
#     return value

# for n in range(1, 1001):
#     print(n, ":", fibonacci(n))


# # Using a built-in function
# from functools import lru_cache

# @lru_cache(maxsize=1000)
# def fibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         return fibonacci(n-1) + fibonacci(n-2)

# for n in range(1, 1001):
#     print(n, ":", fibonacci(n))

# #  converting an Integer to a string in any base
# def to_string(n, base):
#     conver_tString = "0123456789ABCDEF"
#     if n < base:
#         return conver_tString[n]
#     else:
#         return to_string(n//base, base) + conver_tString[n % base]

# print(to_string(2835,16))

# When I think recursion, I think, "Can I describe this problem as a collection of idential subproblems?" If I can, then the definition can be recursive.
# For example, we might identify that "Exploring a node is defined as printing the node then exploring all its neighbors."
# Notice that "exploring" is part of the definition of "exploring"... it's recursive!
# def explore(node):
#     print(node)
#     for n in node.neighbors:
#         explore(n)