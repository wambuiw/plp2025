#function that checks if a number is odd or even and prints the result
def check_even_odd(number):
    if number % 2 == 0:
        print(number,"is even!")
    else:
        print(number,"is odd!")



#number = int(input("enter a number"))
number = 14
check_even_odd(number)