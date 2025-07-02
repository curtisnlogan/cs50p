def main():
    x = float(input('Choose a number: '))  # 'int' converts the 'str' input
    # into 'int'
    # like in maths the inner most parenthesis are figured out first
    y = float(input('Choose a number: '))  # double parens here mean
    # inner function of 'input' is being treated as an arg for outer
    # function which is 'int'
    answer = divide_two_numbers(x, y)
    print(f"{answer:,}")


def divide_two_numbers(num_1, num_2):
    z = round(num_1 / num_2, ndigits=2)  # here i am  modifying a 'round' 
    # function default
    # 'ndigits=' in this case
    # originally i placed all of this inside the print function
    # but remember few lines of code can make it MORE complicated to read
    # fewerl lines of code is not always better
    return z


if __name__ == '__main__':
    main()
wefew