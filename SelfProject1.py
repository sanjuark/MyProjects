#Make a program that asks the user a quantity of dollars, an interest rate and a years quantity. Show in screen in how much the initial capital had been converted 
#with those years transcurred if every year the interest rate is applied 

def total(d, x, n):
    tot = (d *(1+x/100))**abs(n)
    return tot

starting = ''
while starting not in ['Yes', 'yes', 'no', 'No']:
    starting = input("Do you want to start using the program? Yes/No >> ")
    if starting not in ['Yes', 'yes', 'no', 'no']:
        print('Wrong answer, I only accept Yes/No')

def cont():
    contin = ''
    while contin not in ['Yes', 'yes', 'No', 'no']:
        contin = input('You will continue using the program? >> ')
        if contin not in ['Yes', 'yes', 'no', 'No']:
            print('Wrong answer, I only accept Yes/No')
    return contin

while starting in ["Yes", 'yes']:
    print("Enter the quantity of dollars >> ")
    dollars = float(input())
    print('Enter the interest rate percentage >> ')
    interest_rate = float(input())
    print('Enter the quantity of years >> ')
    years = float(input())
    total = total(dollars, interest_rate, years)
    print(f'The convertion of {dollars} dollars in {years} years, with an interest rate of {interest_rate}% is >> {total}')
    
    cont = cont()
    if cont in ['No', 'no']:
        break
    