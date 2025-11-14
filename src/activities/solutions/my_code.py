from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

def describe_dataframe(df):
    """Print information describing the contents of a DataFrame.

        Parameters:
        df (DataFrame): The pandas DataFrame to describe.

        Returns:
        None
    """
    pd.set_option("display.max_columns", None)

    print(df.shape)
    print(df.head())
    print(df.tail())
    print(df.columns)
    print(df.dtypes)
    df.info()
    print(df.describe())

def find_missing_values(df):
    """Print the number of missing values and show rows that contain them.

        Parameters:
        df (DataFrame): The pandas DataFrame to check for missing values.

        Returns:
        None
    """
    print(df.isna().sum())
    missing_rows = df[df.isna().any(axis=1)]
    print(missing_rows)

def plot_histograms(df):
    """Create histograms for selected numerical columns.

        Parameters:
        df (DataFrame): The pandas DataFrame to plot.

        Returns:
        None
    """
    columns = ["participants_m", "participants_f"]
    df[columns].hist()
    plt.show()

def plot_boxplots(df):
    """Create a boxplot for the DataFrame to visualize data spread and outliers.

        Parameters:
        df (DataFrame): The pandas DataFrame to plot.

        Returns:
        None
    """
    df.boxplot()
    plt.show()

def plot_timeseries(df):
    """Plot a timeseries chart showing participants over time.

        Parameters:
        df (DataFrame): The pandas DataFrame to plot.

        Returns:
        None
    """
    # Overall participants trend
    df.plot(x="start", y="participants", title="Total Participants Over Time")
    plt.show()
    
    # Male and Female participants split
    df.plot(x="start", y=["participants_m", "participants_f"], title="Male and Female Participants Over Time")
    plt.show()

def explore_categorical_data(df):
    """Explore categorical columns by printing unique values and their counts.

        Parameters:
        df (DataFrame): The pandas DataFrame to explore.

        Returns:
        None
    """
    # For 'type' column
    print("Distinct categorical values in the event 'type' column")
    print(df['type'].unique())
    print("Count of each distinct categorical value in the event 'type' column")
    print(df['type'].value_counts())

    # For 'disabilities_included' column
    print("Distinct categorical values in the 'disabilities_included' column")
    print(df['disabilities_included'].unique())
    print("Count of each distinct categorical value in the 'disabilities_included' column")
    print(df['disabilities_included'].value_counts())


def prepare_paralympics_data(df):
    """Prepare the Paralympics event data for analysis or dashboard use.

        This function will:
        - Remove columns that are not needed
        - Resolve issues with missing values
        - Change data types
        - Correct categorical data
        - Add new data: new columns, merge datasets

        Parameters:
        df (DataFrame): The raw Paralympics DataFrame.

        Returns:
        DataFrame: The cleaned and prepared Paralympics DataFrame.
    """
    # Remove unwanted columns
    df_prepared = df.drop(columns=['URL', 'disabilities_included', 'highlights'])
    print("Columns after removal:")
    print(df_prepared.columns)

    # Drop missing values
    df_prepared = df_prepared.drop(index=[0, 17, 31])
    df_prepared = df_prepared.reset_index(drop=True)
    print("After dropping rows with missing values:")
    print(df_prepared)

    # Fix categorical errors
    df_prepared.loc[df_prepared['type'] == 'Summer', 'type'] = 'summer'
    df_prepared['type'] = df_prepared['type'].str.strip()
    print("Distinct values in 'type' after cleaning:")
    print(df_prepared['type'].unique())

    # Change float64 to integer type
    columns_to_change = ['countries', 'events', 'participants_m', 'participants_f', 'participants']
    for col in columns_to_change:
        df_prepared[col] = df_prepared[col].astype('Int64')
    print("Data types after changing float columns to Int64:")
    print(df_prepared.dtypes)

    # Change object to date
    print("Unique values in 'start' column before conversion:")
    print(df_prepared['start'].unique())
    print("Unique values in 'end' column before conversion:")
    print(df_prepared['end'].unique())
    df_prepared['start'] = pd.to_datetime(df_prepared['start'], format='%d/%m/%Y')
    df_prepared['end'] = pd.to_datetime(df_prepared['end'], format='%d/%m/%Y')
    print("Data types after changing start/end to datetime:")
    print(df_prepared.dtypes)

    # Add computed column 'duration'
    duration_values = (df_prepared['end'] - df_prepared['start']).dt.days.astype('Int64')
    df_prepared.insert(df_prepared.columns.get_loc('end') + 1, 'duration', duration_values)
    print("New column 'duration' added after 'end':")
    print(df_prepared[['start', 'end', 'duration']])

    # Load NPC codes data
    npc_codes_file_csv = Path(__file__).parent.parent.joinpath('data', 'npc_codes.csv')
    npc_codes_csv_df = pd.read_csv(npc_codes_file_csv, encoding='utf-8', encoding_errors='ignore', usecols=['Code', 'Name'])

    # Replace country names before merging
    replacement_names = {
        'UK': 'Great Britain',
        'USA': 'United States of America',
        'Korea': 'Republic of Korea',
        'Russia': 'Russian Federation',
        'China': "People's Republic of China"
    }
    df_prepared['country'] = df_prepared['country'].replace(to_replace=replacement_names)

    # Merge dataframes on country and Name
    df_prepared = df_prepared.merge(npc_codes_csv_df, how='left', left_on='country', right_on='Name')
    print("Merged DataFrame (country, Code, Name):")
    print(df_prepared[['country', 'Code', 'Name']])

    # Remove 'Name' column after merge
    df_prepared = df_prepared.drop(columns=['Name'])
    print("Final merged DataFrame:")
    print(df_prepared)

    # Save the prepared dataset
    prepared_file_csv = Path(__file__).parent.parent.joinpath('data', 'paralympics_prepared.csv')
    df_prepared.to_csv(prepared_file_csv, index=False)
    print(f"Prepared dataset saved to: {prepared_file_csv}")
    
    return df_prepared


if __name__ == "__main__":
    data_file_csv = Path(__file__).parent.parent.joinpath('data', 'paralympics_raw.csv')
    data_file_excel = Path(__file__).parent.parent.joinpath('data', 'paralympics_all_raw.xlsx')

    paralympics_csv_df = pd.read_csv(data_file_csv)
    paralympics_excel_df_1 = pd.read_excel(data_file_excel)
    paralympics_excel_df_2 = pd.read_excel(data_file_excel, sheet_name=1)

    describe_dataframe(paralympics_csv_df)
    describe_dataframe(paralympics_excel_df_1)
    describe_dataframe(paralympics_excel_df_2)

    find_missing_values(paralympics_csv_df)
    find_missing_values(paralympics_excel_df_1)
    find_missing_values(paralympics_excel_df_2)

    plot_histograms(paralympics_csv_df)
    plot_boxplots(paralympics_csv_df)
    plot_timeseries(paralympics_csv_df)

    explore_categorical_data(paralympics_csv_df)

    prepared_df = prepare_paralympics_data(paralympics_csv_df)

