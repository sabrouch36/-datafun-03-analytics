"""
This script processes the Feedback.xlsx Excel file by:
- Counting the frequency of values in all columns
- Calculating the average for numeric columns
- Writing both results to text files
"""

# Imports
import pandas as pd
import pathlib
from utils_logger import logger

# Constants
DATA_PATH = pathlib.Path("example_data/Feedback.xlsx")
PROCESSED_DIR = pathlib.Path("example_processed")
DOC_COUNT_FILE = PROCESSED_DIR / "excel_feedback_doc_count.txt"
AVERAGE_FILE = PROCESSED_DIR / "excel_feedback_average.txt"

# Ensure processed directory exists
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

def analyze_doc_counts(df: pd.DataFrame):
    with DOC_COUNT_FILE.open("w", encoding="utf-8") as file:
        file.write("Document Frequency Count by Column:\n\n")
        for column in df.columns:
            file.write(f"{column}:\n")
            value_counts = df[column].value_counts()
            for value, count in value_counts.items():
                file.write(f"  {value}: {count}\n")
            file.write("\n")
    logger.info(f"Wrote document counts to {DOC_COUNT_FILE}")

def analyze_column_averages(df: pd.DataFrame):
    numeric_df = df.select_dtypes(include='number')
    means = numeric_df.mean()
    with AVERAGE_FILE.open("w", encoding="utf-8") as file:
        file.write("Column Averages (Mean):\n\n")
        for column, mean in means.items():
            file.write(f"{column}: {mean:.2f}\n")
    logger.info(f"Wrote column averages to {AVERAGE_FILE}")

def main():
    try:
        df = pd.read_excel(DATA_PATH)
        logger.info(f"Excel file loaded: {DATA_PATH}")
        analyze_doc_counts(df)
        analyze_column_averages(df)
    except Exception as e:
        logger.error(f"Error processing Excel file: {e}")

if __name__ == "__main__":
    main()
