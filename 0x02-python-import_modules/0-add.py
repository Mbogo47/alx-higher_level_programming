#!/usr/bin/python3

a = 1
b = 2
add_0 = __import__("add_0")
print("{:d} + {:d} = {:d}".format(a, b, add_0.add(a, b)))
