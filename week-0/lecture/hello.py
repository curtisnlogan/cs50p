def welcome_user(name='curtis logan'):  # 'def' is short for define
    #  how we create our own functions
    # this funciton takes on parameter 'name'
    name = name.strip().title()  # ask user for
    # their name accidental spaces etc. 'strip()' method removes
    # capitalise  method correct capitalisation mistakes from user input
    # these methods can be chanined together as displayed

    first, last = name.split(' ')  # method will grab first and last name as
    # seperate variables

    print(f"hello, {first}", end=".")  # 'end=' overrided
    # default parameter of '\n'


def main():  # convention.all code to be executed in a project for example
    #  normally at the top of a file called 'main'
    # should be contained in a 'main()' function
    welcome_user()


if __name__ == "__main__":  # so-called dunder main, will only run if running
    # this file specifically
    main()  # i am calling the main function here
