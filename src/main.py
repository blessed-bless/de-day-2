# main.py
import logging
from pathlib import Path
from datetime import datetime

from config import Config
from extract import extract_csv
from transform import clean_data, filter_completed, add_calculated_columns, aggregate_by_customer
from load import load_to_csv

def setup_logging():
    """Set up logging configuration."""
    log_file = Config.LOGS_DIR / f"pipeline_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

    logging.basicConfig(
        level=getattr(logging, Config.LOG_LEVEL),
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'  ),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

def run_etl_pipeline():
    """Run the ETL pipeline."""
    logger = setup_logging()
    logger.info("=" * 50)
    logger.info("Starting ETL pipeline")
    logger.info("=" * 50)

    try:
        # Create directories
        Config.create_directories()

        # Extract
        logger.info("\nStep 1: Extract")
        df_raw = extract_csv(str(Config.RAW_FILE))
        logger.info(f"read lines: {len(df_raw)}")

        # Transform
        logger.info("\nStep 2: Transform")

        # Clean
        df_clean = clean_data(df_raw)

        # Filter
        df_filtered = filter_completed(df_clean)

        # Add calculated columns
        df_with_calc = add_calculated_columns(df_filtered)

        logger.info(f"lines after transform: {len(df_with_calc)}lines")

        # Load
        logger.info("\nStep 3: Load")
        load_to_csv(df_with_calc, str(Config.CLEAN_FILE))

        # Aggregate
        logger.info("\nStep 4: Aggregate")
        df_agg = aggregate_by_customer(df_with_calc)
        load_to_csv(df_agg, str(Config.AGG_FILE))

        # Final
        logger.info("\n" + "=" * 50)
        logger.info("Pipeline completed successfully")
        logger.info(f"Cleaned data saved to: {Config.CLEAN_FILE}")
        logger.info(f"Aggregated data saved to: {Config.AGG_FILE}")
        logger.info("=" * 50)

        return True
    
    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        raise

if __name__ == "__main__":
    run_etl_pipeline() 