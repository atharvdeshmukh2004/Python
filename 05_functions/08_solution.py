"""
8. Function with **kwargs
Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

"""
def fun(**kwargs):
    for k, val in kwargs.items():
        print("%s == %s" % (k, val))


# Driver code
fun(s1='Geeks', s2='for', s3='Geeks')