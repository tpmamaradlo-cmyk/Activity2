

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))



def calculate_sum():
    global sum,num1,num2
    sum=num1+num2
    print(f"Sum: {sum}")

def calculate_difference():
    global difference,num1,num2
    difference=num1-num2
    print(f"Difference: {difference}")

calculate_sum()
calculate_difference()



