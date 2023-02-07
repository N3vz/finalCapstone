import math
# Choose the option investment or bond
option = input(
    "Choose either 'investment' or 'bond' from the menu below to proceed:\n ").lower()

# info about investment and bond
print("investment-to calculate the amount of interest you'll earn on your investment")
print("bond-to calculate the amount you'll have to pay on a home loan")


if option == "investment":  # if investment option is selected
    P = float(input("How much do you want to deposit?\n "))
    r = float(input("Enter your interest rate:\n "))/100  # in %
    t = float(input("How many years do you plan on investing?\n "))
    interest = input("Do you want 'simple' or 'compound' interest?\n ").lower()

    if interest == "simple":  # if simple interest is selected
        A = P*(1+r*t)
        print("Monthly repayment:{}".format(A))
    elif interest == "compound":  # if compound interest is selected
        A = P * math.pow((1+r), t)
        print("Monthly repayment:{}".format(A))
    else:
        print("Invalid choice, choose 'simple' or 'compound' interest ")

elif option == "bond":  # if bond is selected
    P = float(input("What is the value of the house?\n "))
    i = float(input("What is your monthly interest rate?\n "))
    # converting i to decimals and dividing by 12 to get the monthy interest rate
    i = float((i/100)*1/12)
    n = float(input("How many months do you plan to take to repay the bond?\n "))
    x = round((i*P)/(1 - (1+i)**(-n)), 2)  # Bond repayment formula

    print("Monthly repayment:{}".format((x)))

else:
    print("Invalid choice")
