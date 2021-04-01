limit = 5
inital= 1
total =0 
def calculation(limit,inital,total):
    x = 0
    equation = x**3
    for x in range(inital,limit+1):
        total= total +equation
    return total
total = calculation(limit,inital,total)
print(total)        
