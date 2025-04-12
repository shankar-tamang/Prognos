import logging
import os

log_directory = os.path.join(os.path.dirname(__file__), '..', 'logs')
os.makedirs(log_directory, exist_ok=True)  # Creates the logs directory if it doesn't exist

log_file = os.path.join(log_directory, 'chain_logs.log')

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)

logger = logging.getLogger(__name__)
