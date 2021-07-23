import sys

a = 1
print(sys.getrefcount(a))
a = 2
print(sys.getrefcount(a))

print(sys.getrefcount(3))
print(sys.getrefcount([]))
