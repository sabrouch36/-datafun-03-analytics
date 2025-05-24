"""
Process a CSV file on 2020 Happiness ratings by country to analyze the `Ladder score` column and save statistics.
"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import csv
import statistics
import sys

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

# TODO: Replace with the names of your folders
FETCHED_DATA_DIR: str = "example_data"
PROCESSED_DIR: str = "example_processed"

#####################################
# Define Functions
#####################################

# TODO: Add or replace this with a function that reads and processes your CSV file

def analyze_ladder_score(file_path: pathlib.Path) -> dict:
    """Analyze the Ladder score column to calculate min, max, mean, and stdev."""
    try:
        # initialize an empty list to store the scores
        score_list = []
        with file_path.open('r') as file:
            # csv.DictReader() methods to read into a DictReader so we can access named columns in the csv file
            dict_reader = csv.DictReader(file)  
            for row in dict_reader:
                try:
                    score = float(row["Ladder score"])  # Extract and convert to float
                    # append the score to the list
                    score_list.append(score)
                except ValueError as e:
                    logger.warning(f"Skipping invalid row: {row} ({e})")
        
        # Calculate statistics
        stats = {
            "min": min(score_list),
            "max": max(score_list),
            "mean": statistics.mean(score_list),
            "stdev": statistics.stdev(score_list) if len(score_list) > 1 else 0,
        }
        return stats
    except Exception as e:
        logger.error(f"Error processing CSV file: {e}")
        return {}

def process_csv_file():
    """Read a CSV file, analyze Ladder score, and save the results."""
    
    # TODO: Replace with path to your CSV data file
    input_file = pathlib.Path(FETCHED_DATA_DIR, "2020_happiness.csv")
    
    # TODO: Replace with path to your CSV processed file
    output_file = pathlib.Path(PROCESSED_DIR, "happiness_ladder_score_stats.txt")
    
    # TODO: Call your new function to process YOUR CSV file
    # TODO: Create a new local variable to store the result of the function call
    stats = analyze_ladder_score(input_file)

    # Create the output directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Open the output file in write mode and write the results
    with output_file.open('w') as file:

        # TODO: Update the output to describe your results
        file.write("Ladder Score Statistics:\n")
        file.write(f"Minimum: {stats['min']:.2f}\n")
        file.write(f"Maximum: {stats['max']:.2f}\n")
        file.write(f"Mean: {stats['mean']:.2f}\n")
        file.write(f"Standard Deviation: {stats['stdev']:.2f}\n")
    
    # Log the processing of the CSV file
    logger.info(f"Processed CSV file: {input_file}, Statistics saved to: {output_file}")
def write_top_scores_chart(stats: list, output_path: pathlib.Path) -> None:
    """
    Create a simple text-based bar chart of top happiness scores.

    Args:
        stats (list): A list of tuples [(country, score), ...]
        output_path (Path): Path to save the text chart

    Returns:
        None
    """
    try:
        with output_path.open('w') as file:
            file.write("Top Happiness Scores (Text-based Bar Chart)\n\n")
            for country, score in stats:
                bar = '*' * int(score * 3)  # scale stars
                file.write(f"{country:<15} | {bar} ({score:.2f})\n")
        logger.info(f"SUCCESS: Bar chart written to {output_path}")
    except Exception as e:
        logger.error(f"Error writing bar chart: {e}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting CSV processing...")
    process_csv_file()
    logger.info("CSV processing complete.")
        # Fetch the CSV
    csv_path = pathlib.Path(FETCHED_DATA_DIR) / "2020_happiness.csv"
    
    # Analyze data
    country_scores = []

    try:
        with csv_path.open('r', encoding='utf-8') as file:
            next(file)  # skip header
            for line in file:
                parts = line.strip().split(',')
                if len(parts) >= 3:
                    country = parts[1].strip('"')
                    try:
                        score = float(parts[2])
                        country_scores.append((country, score))
                    except ValueError:
                        continue

        # Sort and get top 10
        top_countries = sorted(country_scores, key=lambda x: x[1], reverse=True)[:10]
        
        # Output chart
        chart_path = pathlib.Path(PROCESSED_DIR) / "happiness_ladder_score_chart.txt"
        write_top_scores_chart(top_countries, chart_path)

    except Exception as e:
        logger.error(f"Error reading CSV for chart: {e}")
