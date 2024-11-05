n = int(input("enter the integer number : "))

def sum_digits(n):
    sum=0
    num = n
    while(n>0):
        digit = n%10
        sum = sum+digit
        n //=10

    print(f"the sum of the digits of {num} is {sum}")

sum_digits(n)