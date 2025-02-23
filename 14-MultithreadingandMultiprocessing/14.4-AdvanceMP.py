## Advance Mutlithreading Process

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(numbers):
    time.sleep(10) # sleep for 5 seconds
    return f'Numbers:{numbers * numbers}'

numbers = [1,2,3,4,5,6,7,8,9,0]

## Function call with ProcessPoolExecutor

if __name__ == '__main__':

    with ProcessPoolExecutor(max_workers=50) as executor:
        result=executor.map(square_number,numbers)

    for i in result:
        print(i)