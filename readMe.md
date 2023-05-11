# CSV Splitter

This Python script reads in a CSV file and splits it into separate files by entity. Each output file contains rows corresponding to a single entity from the input file. The output files have uppercase column headings.

## Usage

To use this script, follow these steps:

1. Install Python 3.x on your system, if it is not already installed.
2. Save the `main.py` script to a directory on your system.
3. Open a command prompt or terminal and navigate to the directory containing the `main.py` script.
4. Run the script using the following command:

   ```
   python main.py input_file.csv
   ```

   where `input_file.csv` is the path to your input CSV file.

   The script will create separate output files for each unique entity in the input file, named after the entity.

   For example, if the input file contains data for entities `CHLOE` and `Antony-PF`, the script will create two output files: `CHLOE.csv` and `Antony-PF.csv`.

## Requirements

This script requires Python 3.x and the pandas library to be installed. The script has been tested on Python 3.5 and 3.6, but should work on newer versions of Python as well. 

To install the pandas library, run the following command in your command prompt or terminal:

```
pip install pandas
```