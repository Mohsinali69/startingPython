#program to compute the gross pay
hours=(input('please enter hours'))
salary=(input('please enter salary'))




try:
    hrs=float(hours)
    slry=float(salary)

except:
    hrs=10
    slry=10     


gross_Pay=(slry * hrs)
print('pay: ', gross_Pay)