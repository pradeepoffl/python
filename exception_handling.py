'''

def division(a,b):
    out=a/b
    return out

out=division(4,2)
print(out)

out=division(4,0)
print(out)

#a,b=map(int,input("enter two number").split()) # Read input from user
#print(divison(a,b))

'''

def division(a,b):
    try:
        out=a/b
        return out
    except Exception as e:
        return f'When we are dividing {a}/{b}: Facing {e} Error'


a,b=map(int,input("enter two number: ").split(',')) # Read input from user
print(division(a,b))  # input 2,0 to check zerobydivision error