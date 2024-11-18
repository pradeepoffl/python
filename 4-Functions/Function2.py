"""

def odd_even(num):
    ''' 
    *** with print***

    This function named odd_even & returns odd & even with respect to number given by user
    Input: num
    output: odd & even 
    created on 11th may 2024
    Handling exception condition in real time like 
    when a user enter other data type
   
    Q/A: what is difference the parameter and argument?
    when you giving input in function it called parameter ex: def odd_even(num):
    during calling of function its called argument ex odd_even(10);
    Parameter is place holder for argument 
    '''
    if type(num)==int:
        if num%2==0:
            print(f'Even number:={num}')
        else:
            print(f'Odd number:={num}')
    else:
        print("Try with number")

odd_even(10)
odd_even(13)
odd_even('pradeep')

"""
def odd_even(num):
    if type(num)==int:
        if num%2==0:
            return ('Even=',num)
        else:
            return ('odd=',num)
    else:
        return 'try with number again'

output=odd_even(10)
print(output)

result=odd_even('name')
print(result)
