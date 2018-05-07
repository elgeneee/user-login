def username():
    user_name = input("Username:")
    user = 'Elgene'
    while True:
        if user_name == user:
            password()
            break
        else:
            print('Wrong username')
            break
def password():
    passcode = '1234567'
    inputs = []
    while len(inputs) < 5:
        guess = (input("Enter Password:"))
        if guess == passcode:
            print('Welcome Back, Elgene!')
            break
        else:
            print('Try Again: {}'.format(4 - len(inputs)))
            inputs.append(guess)
    else:
        print('Come back again after 24 hours')

username()
