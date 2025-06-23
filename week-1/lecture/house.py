name = input('Whats your name? ')

match name:  # this is a more python way of writing what
    # is below, were the lines would get far too long to be readable
    case 'Harry' | 'Hermoine' | 'Ron':
        print('Gryffindor')
    case 'Draco':
        print('Slytherin')
    case _:
        print('Not matched')

# if name == 'Harry' or name == 'Hermoine' or name == 'Ron':  # consolidated
    # numerous lines into one here
    # print('Gryffindor')
# else:
    # if name == 'Draco':
        # print('Slytherin')
    # else:
        # print('Who?')
