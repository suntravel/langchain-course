# from functools import wraps

# def my_logger(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"Running {func.__name__}...")
#         result = func(*args, **kwargs)
#         print(f"Finished {func.__name__}.")
#         return result
#     return wrapper

# @my_logger
# def add(a, b):
#     return a + b

# print(add.__wrapped__.__name__)  # This will show the original function, not the wrapper
# print(add(5, 10))

# def outer():
#     outer_var = "I am an outer variable"
#     def inner():
#         print(f"Inner function accessing outer variable: {outer_var}")

#     return inner


# invoke_inner = outer()
# invoke_inner()  # This will print: Inner function accessing outer variable: I am an outer variable

# ls = [1, "works", 3.14, {"key": 123}, [5, 6, 7]]

# print(ls[0])  # Output: 1 
# print(ls[1])  # Output: "works"
# print(ls[2])  # Output: 3.14
# print(type(ls[3]))  # Output: {"key": 123}
# print(ls[4])  # Output: [5, 6, 7]

# a = set('abracadabra')
# print(a)  # Output: {'a', 'b', 'c', 'd', 'r'}

# a = (1, list([2, 3, 4]), 5)
# print(a)  # Output: (1, [2, 3, 4], 5)
# print(a[0])  # Output: 1
# print(a[1])  # Output: [2, 3, 4]
# print(a[2])  # Output: 5
# print(type(a[1]))  # Output: <class 'list'>

# a[1].append(99)
# print(a)  # Output: (1, [2, 3, 4, 99], 5) - The list inside the tuple is mutable, so it can be modified


