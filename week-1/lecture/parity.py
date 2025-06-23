def main():
    x = int(input('Pick a number: '))
    if even_or_odd(x):  # truthy by default, no need to add '== True'
        print('odd')
    else:
        print('even')


def even_or_odd(n):
    return n % 2 != 0  # pythonic way to express this
# before it was spread across four lines. just return the question


if __name__ == '__main__':
    main()
