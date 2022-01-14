"""Write a python program to compute a person's income tax. Assume following
tax laws:
• All taxpayers are charged a flat tax rate of 20%.
• All taxpayers are allowed a $10,000 standard deduction.
• For each dependent, a taxpayer is allowed an additional $3,000 deduction.
• Gross income must be entered to the nearest penny.
Gross Income and the number of dependents must be asked from the user.
Hint:
Taxable income = Gross Income - Standard deduction - (Dependent deduction
* No. of dependents)
Tax = Taxable Income * Tax Rate"""
a=input("enter your income")
b=input("enter your no of dependent \n")
print("tax you have to pay")
print((int(a)-10000-(int(b)*3000))/5)