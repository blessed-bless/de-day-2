# src/con=fig.py
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration project settings."""

    #directory of the project
    BASE_DIR = Path(__file__).parent.parent
    DATA_DIR = BASE_DIR / os.getenv('DATA_DIR', 'data')
    LOGS_DIR = BASE_DIR / os.getenv('LOGS_DIR', 'logs')

    # Files
    RAW_FILE = BASE_DIR / os.getenv('RAW_FILE', 'data/raw_sales.csv')
    CLEAN_FILE = BASE_DIR / os.getenv('CLEAN_FILE', 'data/clean_sales.csv')
    AGG_FILE = BASE_DIR / os.getenv('AGG_FILE', 'data/aggregated_sales.csv')

    #logging settings
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

    @classmethod
    def create_directories(cls):
        """Create necessary directories if they don't exist."""
        cls.DATA_DIR.mkdir(parents=True, exist_ok=True)
        cls.LOGS_DIR.mkdir(parents=True, exist_ok=True)