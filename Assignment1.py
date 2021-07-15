# Declaring variables

fname=input("Enter first name ")
lname=input("Enter last name ")
empnum=input("Enter employee number ")
basicsalary=int(input("Enter Basic Salary "))
totalallowance=int(input("Enter Total allowance "))
totaldeduction=int(input("Enter Total deduction "))

print("Full name is ",fname + lname)
print("Salary in hand is ",(basicsalary + totalallowance)- (totaldeduction))

