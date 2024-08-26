import logging
import os

# Create a logger string
logging_str = "%(asctime)s: %(levelname)s: %(module)s: %(message)s"

log_folder = "logs"
log_file="logs/running_log.log"
os.makedirs(log_folder,exist_ok=True)

#log_file = os.path.join(log_folder, "running_log.log")  # Use os.path.join for cross-platform compatibility

# Create the log directory if it doesn't exist
#os.makedirs(log_folder,exist_ok=True)

# Set up basic logging configuration
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_file)
    ]
    
)

logger = logging.getLogger("mylog")

def add_number(a, b):
    out = a + b
    logger.info(f"Adding {a} and {b}, Result: {out}")  # Log details about the operation
    return out

# Execute the function and print the result
a,b = map(int,input('enter two numbers:').split())
print(add_number(a,b))















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
