
def user_input(prompt):
    while True:
        try:
            return (input(prompt))
        except ValueError:
            print('Invalid input. Please enter a number.')