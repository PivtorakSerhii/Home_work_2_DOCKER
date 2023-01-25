def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def my_app():
    while True:
        user_msg = int(input('Input some number from 0 to 9:'))
        if user_msg == 0:
            print(f"You number is {user_msg}. This command to exit!")
            break
        print(f"Number is {user_msg}. Let`s go to new number!")


if __name__ == '__main__':
    print_hi('PyCharm!')
    my_app()

