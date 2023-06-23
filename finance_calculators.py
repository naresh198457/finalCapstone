''' create a program that allows the user to access two
different financial calculators: an investment calculator and a home loan
repayment calculator. this is thj'''

import math

print('Investment\t- to calculate the amount of interest you\'ll earn on your investment.\nbond\t\t- to calculate the amount you\'ll have to pay on a home loan.')

# Create the methode variable
Method=input('Enter either \'investment\' or \'bond\' from the menu above to proceed: ')
Method=Method.upper()
count=0

# Using the while loop, avoid the Methode typo errors
while Method=='INVESTMENT' or 'BOND':

    match Method:
        case 'INVESTMENT':
            #The amount of money that they are depositing
            P=int(input('How much you want to deposit: '))

            # The interest rate (as a percentage)
            r=float(input('Interest rate (%): '))/100

            # The number of years they plan on investing
            t=int(input('How many years: '))

            # create interest methode variable: simple or compond 
            interest=input('Enter either the \'simple\' or \'compound\' interest: ')
            interest=interest.upper()
            
            # While loop is used 
            while interest=='SIMPLE' or 'COMPOUND':
                if interest=='SIMPLE':
                    Total=round(P*(1+r*t),1) # total amount with simple interest
                    break
                elif interest=='COMPOUND':
                    Total=round(P*math.pow((1+r),t),1) # total amount with compound interest                    
                    break
                
                # if there is spelling mistake, repeating this process until it corrects.
                interest=input('Enter either the \'simple\' or \'compound\' interest. please make sure the spelling is correct: ')
                interest=interest.upper()
                pass

            print(f'After depositing {P} for {t} years with {interest} interest of {r*100}%, you will receive the total amount of {Total}')       
            break
        
        case 'BOND':
            # variables
            P=int(input('Enter the House value (£): '))
            i=float(input('Enter the interest rate (%): '))/100/12
            n=int(input('Enter the no of months remaining:  '))

            repayment=(i*P)/(1-(1+i)**(-n))
            print(f'The monthly repayment will be {round(repayment,1)}£ for next {n} months with interest of {round(i*12*100,1)}.')
            break
    
    # if the 
    if count<5:
        Method=input('Select the \'investment\' or \'bond\'. please make sure the spelling is correct: ')
        Method=Method.upper()
    else:
        print('The program is closed due to incorrect entry for 6 time. Restart the program.')
        break
    count=count+1
