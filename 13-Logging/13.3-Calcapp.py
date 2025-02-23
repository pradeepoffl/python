import logging
import os

# Create a logger string
logging_str = "%(asctime)s: %(name)s: %(levelname)s: %(module)s: %(message)s"

log_folder = "Logs"
log_file="Logs/calcapp.log"
os.makedirs(log_folder,exist_ok=True)

#log_file = os.path.join(log_folder, "running_log.log")  # Use os.path.join for cross-platform compatibility

# Create the log directory if it doesn't exist
#os.makedirs(log_folder,exist_ok=True)

# Set up basic logging configuration
logging.basicConfig(
    level=logging.DEBUG,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]   
)

# creating module logger
logger = logging.getLogger("Arithmethic APP")



def add(a, b):
    result = a + b
    logger.debug(f"Adding {a} + {b} = {result}")  # Log details about the operation
    return result


def substract(a, b):
    result = a - b
    logger.debug(f"substract {a} - {b} = {result}")  # Log details about the operation
    return result

def multiply(a, b):
    result = a * b
    logger.debug(f"multiply {a} * {b} = {result}")  # Log details about the operation
    return result

def divide(a, b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} / {b} = {result}")  # Log details about the operation
        return result   
    except ZeroDivisionError:
        logger.error(f"Error: Division by zero is not allowed")  # Log an error messag
        return None
    


# Execute the function and print the result
a,b = map(int,input('enter two numbers:').split())
print(add(a,b))

print(substract(10,5))
print(multiply(10,5))
print(divide(5,19))





 







'''
import logging 
import os # automatically delete,create files 

#create a logger string

logging_str="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_folder="logs"
log_files="logs/running_log.log"

os.makedirs(log_folder,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[logging.FileHadler(log_files)]
)
logger=logging.getLogger("Mylog")

def add_number(a,b):
    output=a+b
    logger.info("Successfully executed")
    return output

num=add_number(3,4)
print(num)
'''
'''
you’ll need to invest a little more of your time in reading the following docs.
If you’re ready for that, have some water and carry on.

Resource: https://docs.python.org/3/howto/logging.html


'''

'''
def add_number(a,b):
    output=a+b
    print("Successfully executed")
    return output

num=add_number(3,4)
print(num)

'''
