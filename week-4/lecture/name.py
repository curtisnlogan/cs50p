import sys

if len(sys.argv) < 2:
    raise IndexError("Too few")
# or
    sys.exit("Too few")
elif len(sys.argv) > 2:
    raise IndexError("Too many")
# or
    sys.exit("Too many")


print("hello, my name is", sys.argv[1])

for arg in sys.argv[1:]:
    print("hello, my name is", arg)
