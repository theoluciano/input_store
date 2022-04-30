input_lib = []


def print_lib():
    for item in input_lib:
        print(item)


def file_input(user_input):
    input_lib.append(str(user_input))


def get_name():
    user_name = input('Please enter your name: ')
    return user_name


def new_input():
    while True:
        answer = input("Would you like to add more wisdom?(y/n): ")
        if answer == "y" or answer == "Y":
            return True
        elif answer == 'n' or answer == 'N':
            return False
        else:
            print("Invalid input. Please try again!")
            continue


def take_input(user_name):
    got_input = input(str(user_name) + ', please enter something wise. It will be recorded for all eternity:')
    file_input(got_input)


def main():
    name = input('Please enter your name:')
    take_input(name)
    while new_input():
        take_input(name)
        print_lib()
    print("Thanks for your brain cells, buddy! Bye bye!")


main()
