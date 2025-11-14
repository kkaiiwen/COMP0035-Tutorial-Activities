""" Examples of docstring styles and functions and class that are un-documented. """
import sqlite3

import pandas as pd
from matplotlib import pyplot as plt
from contextlib import redirect_stdout

# Google-style docstring specification: https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings
def get_column_names_g(db_path: str, table_name: str) -> list:
    """Retrieves a list of column names for the specified database table.

    Args:
        db_path: Path to the database file
        table_name: Name of the table

    Returns:
        col_names: List of column names
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name});")
    col_names = [row[1] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return col_names


# Numpy-style docstring: https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard
def get_column_names_n(db_path: str, table_name: str) -> list:
    """
        Retrieves a list of column names for the specified database table.

        Parameters
        ----------
        db_path : str
            Path to the database file.
        table_name : str
            Name of the table.

        Returns
        -------
        col_names: list
            List of column names.
        """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name});")
    col_names = [row[1] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return col_names


# Sphinx/reStructuredText style docstring: https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html
# AI prompt:   /doc Sphinx format docstring
def get_column_names_s(db_path: str, table_name: str) -> list:
    """
        Retrieves a list of column names for the specified database table.

        :param db_path: Path to the database file.
        :type db_path: str
        :param table_name: Name of the table.
        :type table_name: str
        :return: List of column names.
        :rtype: list
        """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name});")
    col_names = [row[1] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return col_names


# Copilot in VSCode / PyCharm
# Place the cursor under the function name and generate a docstring e.g. '/doc Google-style docstring'
def generate_histogram(df: pd.DataFrame):
    """Generate and save histograms for the Paralympics dataset.

    Creates several histogram visualizations from the provided DataFrame:
      1. Histograms for all numeric columns.
      2. Histograms specifically for 'participants_m' and 'participants_f'.
      3. Histograms for the subset of data where the 'type' is 'summer'.

    Each histogram is saved to the 'output' directory as a PNG image.

    Args:
        df (pd.DataFrame): The DataFrame containing Paralympics event data.
    """
    # Histogram of any columns with values of a data type that can be plotted
    df.hist(
        sharey=False,  # defines whether y-axes will be shared among subplots.
        figsize=(12, 8)  # a tuple (width, height) in inches
    )
    plt.savefig("output/histogram_df.png")

    # Histograms of specific columns only
    df[["participants_m", "participants_f"]].hist()
    plt.savefig("output/histogram_participants.png")

    # Histograms based on filtered values
    summer_df = df[df['type'] == 'summer']
    summer_df.hist(sharey=False, figsize=(12, 8))
    plt.savefig("output/histogram_summer.png")


# Copilot in VSCode / PyCharm
# If you are happy to use gen-AI tools, place the cursor under the docstring and ask the AI to generate the code
def describe(csv_data_file: str) -> dict:
    """Opens the data as a pandas DataFrame applies pandas functions to describe the data.

    Applies the following pandas functions to the DataFrame and prints the output to file instead of terminal:
        df.shape
        dd.head(num)
        df.tail(num)
        df.columns
        df.dtypes
        df.describe()
        df.info()

       Args:
       csv_data_file (str): File path of the .csv format data file.
    """
    # Load CSV file as DataFrame
    df = pd.read_csv(csv_data_file)

    # Redirect all print output to a file instead of the terminal
    with open("output/describe.txt", "w") as f:
        with redirect_stdout(f):
            print("=== DataFrame Description ===\n")
            print("Shape:", df.shape)
            print("\nHead:\n", df.head())
            print("\nTail:\n", df.tail())
            print("\nColumns:\n", df.columns)
            print("\nData Types:\n", df.dtypes)
            print("\nDescriptive Statistics:\n", df.describe())
            print("\nInfo:")
            df.info()