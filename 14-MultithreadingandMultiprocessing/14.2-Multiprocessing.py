## Multiprocess: A Multiprocessor Architecture for Real-Time Systems that runs in parallel, which help the overall performance of system
## CPU-Bound Task: Task which are executed by heavy CPU usage i.e mathematical computation, data processing.
## Parallel exection - Multiple cores of CPU

import multiprocessing
import time

# Function to be executed in parallel

def square():
    for i in range(5):
        time.sleep(2)
        print(f'Number:{i}')
        print(f'Square:{i*i}')

def cube():
    for i in range(5):
        time.sleep(2)
        print(f'Cube:{i*i*i}')   

if __name__ == '__main__':

    ## Create a process for square and cube function
    p1 = multiprocessing.Process(target=square)
    p2 = multiprocessing.Process(target=cube)

    ## Start the process
    start_time = time.time()
    print(f'Start Time:{start_time}')
    p1.start()
    p2.start()

    ## Wait until both processes finish
    p1.join()
    p2.join()
    end_time = time.time()

    print(f'End Time:{time.time()}')
    print(f'Total execution time:{end_time - start_time}')
