import logging
import logging.config
import json
import yaml
import logmatic

# Simple logging
logging.warning('I will be back!')

# Set DEBUG log level
# Add timestamps to the log lines
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

logging.debug('Hi')
logging.debug('Addition of %s and %s produces %s', 1, 2, 1+2)

# Create logger
logger = logging.getLogger('logger_name')
logger = logging.getLogger(__name__)

# Create root logger
root = logging.getLogger()

# Set logger log level
root.setLevel(logging.INFO)

# Create console handler
console = logging.StreamHandler()
root.addHandler(console)

# Create file handler
fileHandler = logging.FileHandler('logging.log')
logger.addHandler(fileHandler)

# Create rotating file handler
rotatingFileHandler = logging.handlers.RotatingFileHandler('logging.log', 'a', 300, 10)
logger.addHandler(rotatingFileHandler)

# Set handler log level
console.setLevel(logging.ERROR)

# Set handler formatter
formatter = logging.Formatter('%(asctime)s : %(name)-12s : %(relativeCreated)6d %(threadName)s : %(levelname)-8s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
console.setFormatter(formatter)

# Log info & error
root.info('Hello World')
root.error('Hello World!')

# Load the logging configuration
# logging.config.fileConfig('logging.ini')
logging.config.dictConfig(json.load(open('logging.json')))
# logging.config.dictConfig(yaml.safe_load(open('logging.yml').read()))

# Log
logger.info('Info message')

# Log with Traceback
try:
    raise Exception()
except Exception as e:
    logger.error('Error message', exc_info=True)

try:
    raise Exception()
except Exception as e:
    logger.exception('Exception message')
