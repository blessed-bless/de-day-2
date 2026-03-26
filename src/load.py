#src/load.py
import pandas as pd
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def load_to_csv(df: pd.DataFrame, file_path: str, index: bool = False) -> None:
    """
    Load a DataFrame to a CSV file.

    Args:
        df (pd.DataFrame): The DataFrame to be loaded.
        file_path (str): The path to the output CSV file.
        index (bool): Whether to write row names (index). Default is False.
    """
    logger.info(f"Loading data to {file_path}")
    
    try:
       # create directory if it doesn't exist
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)

        # save the DataFrame to a CSV file
        df.to_csv(file_path, index=index)
        logger.info(f"Data successfully {len(df)} lines")
    except Exception as e:
        logger.error(f"Error loading: {e}")
        raise


def load_to_dict(df: pd.DataFrame) -> dict:
    """
    Converting a DataFrame to a Dictionary (for API)

    Args:
        df: pd.DataFrame
         
    Returns:
        Dictionary with data
    """
    logger.info("Converting DataFrame to dictionary")
    data_dict = df.to_dict('records')
    logger.info(f"Converted {len(data_dict)} lines to dictionary")
    return data_dict

if __name__ == "__main__":
    # Text
    logging.basicConfig(level=logging.INFO)
    import extract, transform
    df = extract.extract_csv("../data/raw_sales.csv")   
    df_clean = transform.clean_data(df)
    load_to_csv(df_clean, "../data/clean_sales.csv")