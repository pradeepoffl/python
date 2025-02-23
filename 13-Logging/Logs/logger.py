# Configuring logging
import logging
logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    filemode='w',
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    
)