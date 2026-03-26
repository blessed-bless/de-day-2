# src/transform.py
import pandas as pd
import logging

logger = logging.getLogger(__name__)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the input DataFrame by handling missing values and converting data types.

    Args:
        df (pd.DataFrame): The input DataFrame to be cleaned.
        
        Returns:
        Cleaned DataFrame.
        """
    logger.info("Cleaning data")
    
    # Delete duplicates
    df = df.drop_duplicates()
    logger.info(f"Removed duplicates. Remaining rows: {len(df)}")
    
    # Handle missing values
    df = df.dropna()
    logger.info(f"Removed missing values. Remaining rows: {len(df)}")

    return df
def filter_completed(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filter the DataFrame to include only completed sales.

    Args:
        df (pd.DataFrame): The input DataFrame to be filtered.
        
    Returns:
        Filtered DataFrame containing only completed sales.
    """
    logger.info("Filtering completed sales")
    df_filtered = df[df['status'] == 'completed'].copy()
    logger.info(f"Found {len(df_filtered)} completed sales")
    return df_filtered

def add_calculated_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add calculated columns to the DataFrame, such as total price.

    Args:
        df (pd.DataFrame): DataFrame whith sales data.
        
        returns:
        DataFrame with added calculated columns.
        """
    logger.info("Adding calculated columns")
    
    # Copy it so as not to change the original
    df = df.copy()

    # Tax 10%
    df['tax'] = df['amount'] * 0.10

    # Total price with tax
    df['total'] = df['amount'] + df['tax']

    logger.info("Added calculated columns: tax and total")
    return df

def aggregate_by_customer(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate sales data by customer
    
    Args:
        df: DataFrame with sales data.
        
    Returns: 
        Aggregated DataFrame
    """
    logger.info("Aggregating sales data by customer")

    df_agg = df.groupby('customer_id').agg(
        total_orgers=('order_id', 'count'),
        total_amount=('amount', 'sum'),
        avg_amount=('amount', 'mean')
    ).reset_index()

    logger.info(f"Aggregated data for {len(df_agg)} customers")
    return df_agg

if __name__ == "__main__":
    # Test
    logging.basicConfig(level=logging.INFO)
    import extract
    df = extract.extract_csv("../data/raw_sales.csv")
    df_clean = clean_data(df)
    print(df_clean.head())