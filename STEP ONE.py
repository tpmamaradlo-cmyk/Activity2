#Get First and Second number

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))


#Get Sum
def calculate_sum():
    global sum
    sum=num1+num2
    print(f"Sum: {sum}")

#Get Difference
def calculate_difference():
    global difference
    difference=num1-num2
    print(f"Difference: {difference}")

#call functions
calculate_sum()
calculate_difference()



