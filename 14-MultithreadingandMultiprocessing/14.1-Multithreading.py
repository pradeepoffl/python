## Multithreading 
## When to use multithreading
## IO -bound tasks: Tasks that spend more time waiting IO operations (e.g., reading/writing files, network requests) can be executed in parallel using multithreading
## Concurrent Execution: When you want to improve the throughput of your application by performing multiple operations concurrently.

import threading
import time

# Define function are handled by single thread in single flow line-by-line execution
# We will define two thread functions 

def print_numbers():
    for i in range(5):
        time.sleep(2) # Simulate IO-bound task
        print(f'Number:{i}')

def print_letters():
    for i in "abcde":
        time.sleep(2) # Simulate IO-bound task
        print(f'Letter:{i}')

## Create threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

## calling threads
start_time = time.time()
print(f'Start Time:{start_time}')
t1.start()
t2.start()

## wait for both threads to finish
t1.join()
t2.join()

End_time=time.time()
print(f'End Time:{End_time}')
print(f'Program execution time:{End_time-start_time}')




'''
## single thread Flow execution by default

## calling functions
## Understand the time taken for execution

start_time = time.time()
print(f'Start time:{start_time}')
print_numbers()
print_letters()
end_time=time.time()
print(f'End time:{end_time}')
print(f'Total time taken:{end_time-start_time}')


'''