# importing necessary module
import time as t

# function to calculate Truncation error
def Truncation_err():

    x = float(input('\nEnter the true value of number : '))
    y = float(input('\nEnter the approximate value : '))

    Et = abs(x - y)

    wait = int(input('\nHow much seconds would you like to wait to check the answer : '))

    sig_plc = int(input('\nHow much accuracy do you want after decimal places : '))

    print(round(Et, sig_plc))

    t.sleep(wait)

    return Et

# function to calculate Absolute error
def Absolute_err():

    x = float(input('\nEnter the true value of number : '))
    y = float(input('\nEnter the approximate value : '))

    Ea = abs(x - y)

    wait = int(input('\nHow much seconds would you like to wait to check the answer : '))

    sig_plc = int(input('\nHow much accuracy do you want after decimal places : '))

    print(round(Ea, sig_plc))

    t.sleep(wait)

    return Ea

# function to calculate Relative error
def Relative_err():

    x = float(input('\nEnter the true value of number : '))
    y = float(input('\nEnter the approximate value : '))

    Er = abs((x - y)/x)

    wait = int(input('\nHow much seconds would you like to wait to check the answer : '))

    sig_plc = int(input('\nHow much accuracy do you want after decimal places : '))

    print(round(Er, sig_plc))

    t.sleep(wait)

    return Er

# function to calculate percentage error
def Percentage_err():

    x = float(input('\nEnter the true value of number : '))
    y = float(input('\nEnter the approximate value : '))

    Ep = abs((x - y)/x)*100

    wait = int(input('\nHow much seconds would you like to wait to check the answer : '))

    sig_plc = int(input('\nHow much accuracy do you want after decimal places : '))

    print(round(Ep, sig_plc))

    t.sleep(wait)

    return Ep

# main function
def main():

    while True:

        print('\n\nWHICH ERROR YOU WANT TO CALCULATE ?')
        print('\n1> Truncation Error')
        print('2> Absolute Error')
        print('3> Relative Error')
        print('4> Percentage Error')
        print('5> Exit')
        choice = int(input('\nEnter your choice : '))

        if choice == 1:
            Truncation_err()

        elif choice == 2:
            Absolute_err()

        elif choice == 3:
            Relative_err()

        elif choice == 4:
            Percentage_err()

        elif choice == 5:
            break

# Using the special variable 
if __name__=="__main__":
    main()