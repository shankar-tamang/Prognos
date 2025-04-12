import json
from utils.logging_utils import logger

def save_state_to_file(state, file_path):
    try:
        with open(file_path, 'w') as f:
            json.dump(state, f)
        logger.info("Conversation state saved successfully.")
    except Exception as e:
        logger.error(f"Failed to save conversation state: {e}")

def load_state_from_file(file_path):
    try:
        with open(file_path, 'r') as f:
            state = json.load(f)
        logger.info("Conversation state loaded successfully.")
        return state
    except Exception as e:
        logger.error(f"Failed to load conversation state: {e}")
        return {}
