## Advance Multithreading with ThreadPoolExecutor

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(numbers):
    time.sleep(5) # sleep for 5 seconds
    return f'Numbers:{numbers}'

numbers = [1,2,3,4,5,6,7,8,9,0]

with ThreadPoolExecutor(max_workers=10) as executor:
    result=executor.map(print_number,numbers)

for i in result:
    print(i)