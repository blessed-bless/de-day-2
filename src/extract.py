# src/extract.py
import pandas as pd
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def extract_csv(file_path: str) -> pd.DataFrame:
    """
    Extract data from a CSV file.
    
    Args:
    Checking the environment
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: A DataFrame containing the extracted data.
    """
    logger.info(f"Extracting data from {file_path}")

    try:
        df = pd.read_csv(file_path)
        logger.info(f"successfully read {len(df)} lines")
        return df
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise
    except Exception as e:
        logger.error(f"An error occurred while reading the file: {e}")
        raise
    """
    Creating a DataFrame from a Dictionary (for testing)
    
    Args: Dictionary with data
    
    Returns:
    Dataframe
    """
    logger.info("Creating DataFrame from dictionary")
    df = pd.DataFrame(data)
    logger.info(f"Created {len(df)} lines")
    return df

if __name__ == "__main__":
    # Text
   logging.basicConfig(level=logging.INFO)
   df = extract_csv("../data/raw_sales.csv")
   print(df.head())