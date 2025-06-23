def main():
    print_squares(3)


# this funciton allows me to print a brick 3 columns wide
# and 3 rows long
def print_squares(n):
    for i in range(n):
        print("#" * n)


main()


print("end of last function")


def print_brick_column(n_height):
    print("#\n" * n_height)  # more pythonic way of doing this
    # instead of using loops


def main():
    print_brick_column(3)


main()
