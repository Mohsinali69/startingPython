hours=float(input('please enter how many hours you worked : '))
pay=float(input('please enter your salary : '))

def computepay(h,p):
    if h>40:
        salary= (h-40)*(1.5*p)+(40*p)
    else :
        salary=h*p
    
    return salary

total=computepay(hours,pay)
print(total)