import math                                                                             # import math module
print("""
investment - to calculate the amount of interest you'll earn on your investment 
bond       - to calculate the amount you'll have to pay on a home loan

Enter either 'investment' or 'bond' from the menu above to proceed:""")                 #print instrucions for user

task = input("Enter here:").lower()                                                     #input for user, changes sting to lower case 

                                                                                        # if statement depending on what the user inputs above
if task == "bond":                                                                      # if bond is chosen
    P = int(input("Enter the present value of the house: "))                            # Present value of house
    r = int(input("Enter the interest rate: "))
    i = r/(100 * 12)                                                                    # Monthly interest 
    n = int(input("Enter the number of months you plan to take to repay the bond: "))   # Number of months over which the bond will be repaid:

                                                                                        # The amount that a person will have to be repaid
                                                                                        # on a home loan each month is calculated as follows:
    repayment = (i * P)/(1 - (1 + i)**(-n))
    repayment = "{:.2f}".format(round(repayment, 2))                                    # Rounds repayment to 2 decimal place
    print(f"Your monthley repayment: £{repayment}")
    
elif task == "investment":                                                              # If invetment is chosen
    P = int(input("Enter the amount of money that you are depositing: "))               # Amount user deposits
    r = int(input("Enter the interest rate: "))
    r = r/100                                                                           # The interest rate
    t = int(input("Enter the number of years you plan on investing: "))                 # Number of years of investment
    
    interest = input("Would you want simple or compound interest? ").lower()            # Using values above, calculate interest of choice
    
    if interest == "simple":                                                            # If simple interest is input above the following block is run
        A = P*(1 + r*t)                                                                 # Calculates total amount once the interest has been applied
        A = "{:.2f}".format(round(A, 2))                                                # Rounds answer to 2dp
        print (f"Total ammount after interest: £{A}")

    elif interest == "compound":                                                        # If compound interest is input above, then the following block is run
        A = P * math.pow((1+r),t)                                                       # Calculates total amount once the interest has been applied, uses math.pow() to rais to power of t 
        A = "{:.2f}".format(round(A, 2))                                                # Rounds answer to 2dp
        print (f"Total ammount after interest: £{A}")

    else:
        print("ERROR: You have not entered a correct option")                           # Gives error message when incorrect option is input

else:
    print("ERROR: You have not entered a correct option")