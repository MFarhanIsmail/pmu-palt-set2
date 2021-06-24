#palt python set 2
#question1
#Mohamad farhan bin ismail (20ddt19f1085)
print('Please enter correct password to continue:')
attemp=0
while attemp < 5:
    password = input('Enter password: ')
    if password=='farhan12345':
        print('password is correct Access granted')
        break
    else:
        print('The password is wrong please try again.')
        attemp += 1