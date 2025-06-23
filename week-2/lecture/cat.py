# python doesn't come with a 'meow' function so lets create one!
# allot of programming is about creating your own or using
# third party functions
# 'n' typically used as a placeholder parameter, if no specific name
# fits
def main():
    n = get_number()
    meow(n)


def meow(n):
    for _ in range(n):
        print("meow")


def get_number():
    n = input("Whats n?: ")
    if n > 0:
        return  # we need to return a value here, not 'break' the infinite loop


# infinite loop solution to undesired user input
# only escape loop if input doesnt break some specified conditionals
while True:
    n = int(input("Whats n? "))
    if n > 0:
        # takes you out of the infinite loop
        break

for _ in range(n):
    print("mmmeow")

# interesting way to do the below in python
# perhaps has readability issues depending on who you ask
print("meow!!!\n" * 3, end="")

# better way to do this, easy to adjust the amount of mewos
# naming '_' is python if you just need something generic to
# iterate over
for _ in range(10):
    print("meow!")

# might not be the best way to do this, what if
# i wanted to do say 10 meows
for i in [0, 1, 2]:
    print("Meow!")

# good habit to start at '0' and not go through the
# value that you want to stop at
i = 0
# simple 'while' loop that only stops
# when 'i' == '1'
while i < 3:
    print("meow")
    # more pythonic than 'i = i - 1'
    i += 1
