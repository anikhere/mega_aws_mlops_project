import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd,'logs',LOG_FILE)
os.makedirs(os.path.dirname(log_path))
logging.basicConfig(
    filename=LOG_FILE,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
)
logger = logging.getLogger(__name__)
