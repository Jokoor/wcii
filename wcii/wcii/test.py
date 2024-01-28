def my_map(x):
    return x**2  

nums = [1, 2, 3, 4, 5]
x = [my_map(num) for num in nums]
print(list(x))