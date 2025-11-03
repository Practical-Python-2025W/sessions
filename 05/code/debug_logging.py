import logging

# Configure logging settings
logging.basicConfig(
    level=logging.DEBUG,  # Set the minimum log level to DEBUG
    format='%(asctime)s - %(levelname)s - %(message)s', # Define the log message format
    filename='bike_app.log'
)

# Example log messages
logging.debug('This is a debug message')  # Detailed information for debugging
logging.info('This is an info message')  # General information
logging.warning('This is a warning message')  # Potential issue
logging.error('This is an error message')  # Error that affects functionality
logging.critical('This is a critical message')  # Serious error