import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os

"""
EDA Tool

This script is designed to help users perform exploratory data analysis (EDA) interactively via the terminal.
Users can load their dataset, compute descriptive statistics, and generate various visualizations to understand
their data better. The functionalities include:

- Computing descriptive statistics (mean, median, mode, standard deviation, quartiles).
- Displaying available columns in the dataset.
- Plotting histograms, box plots, and scatter plots.
- Calculating confidence intervals for sample means.

Usage:
1. Run the script using Python:
   python EDA_script.py
2. Follow the prompts to enter the file path and select the type of analysis or visualization.

Requirements:
- pandas
- numpy
- matplotlib
- seaborn
- scipy
"""

def compute_descriptive_stats(df):
    """
    Compute descriptive statistics for a given DataFrame.
    
    Parameters:
    df (pandas.DataFrame): The input DataFrame containing the data.
    
    Returns:
    pandas.DataFrame: A DataFrame containing the mean, median, mode, standard deviation, and quartiles.
    """
    numeric_df = df.select_dtypes(include=[np.number])  # Select only numeric columns
    stats_dict = {
        'Mean': numeric_df.mean(),
        'Median': numeric_df.median(),
        'Mode': numeric_df.mode().iloc[0],  # Select the first mode
        'Standard Deviation': numeric_df.std()
    }
    
    quartiles = numeric_df.quantile([0.25, 0.5, 0.75])
    for q in quartiles.index:
        stats_dict[f'Quartile {int(q*100)}%'] = quartiles.loc[q]
    
    return pd.DataFrame(stats_dict)

def show_available_columns(df):
    print(df.columns.tolist())

def info(df):
    print(df.info())

def plot_histogram(df, column):
    """
    Plot a histogram for a specified column in the DataFrame.
    
    Parameters:
    df (pandas.DataFrame): The input DataFrame containing the data.
    column (str): The column name for which the histogram is to be plotted.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True)
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

def plot_boxplot(df, column):
    """
    Plot a box plot for a specified column in the DataFrame.
    
    Parameters:
    df (pandas.DataFrame): The input DataFrame containing the data.
    column (str): The column name for which the box plot is to be plotted.
    """
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=df[column])
    plt.title(f'Box Plot of {column}')
    plt.xlabel(column)
    plt.show()

def plot_scatter(df, column1, column2):
    """
    Plot a scatter plot for two specified columns in the DataFrame.
    
    Parameters:
    df (pandas.DataFrame): The input DataFrame containing the data.
    column1 (str): The column name for the x-axis.
    column2 (str): The column name for the y-axis.
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=df[column1], y=df[column2])
    plt.title(f'Scatter Plot of {column1} vs {column2}')
    plt.xlabel(column1)
    plt.ylabel(column2)
    plt.show()

def compute_confidence_interval(df, column, confidence=0.95):
    """
    Compute the confidence interval for the mean of a specified column in the DataFrame.
    
    Parameters:
    df (pandas.DataFrame): The input DataFrame containing the data.
    column (str): The column name for which the confidence interval is to be computed.
    confidence (float): The confidence level for the interval (default is 0.95).
    
    Returns:
    tuple: A tuple containing the mean, lower bound, and upper bound of the confidence interval.
    """
    # Ensuring that the column chosen is numeric.
    if not pd.api.types.is_numeric_dtype(df[column]):
        raise ValueError(f"Column '{column}' is not numeric and cannot be used to compute a confidence interval.")
    
    data = df[column].dropna()  # Remove NaN values from the column
    mean = data.mean()  # Calculate the mean of the column
    sem = stats.sem(data)  # Calculate the standard error of the mean
    margin_of_error = sem * stats.t.ppf((1 + confidence) / 2., len(data)-1)  # Calculate the margin of error
    return mean, mean - margin_of_error, mean + margin_of_error  # Return the mean and the confidence interval bounds

def main():
    """
    Main function to interact with the user via the terminal and perform EDA on the specified dataset.
    """
    print("Welcome to the EDA Tool!")
    file_path = input("Please enter the full path to your dataset (CSV file): ")
    
    # Check if the file exists
    if not os.path.isfile(file_path):
        print("The file does not exist. Please check the file path and try again.")
        return
    
    # Load the dataset
    df = pd.read_csv(file_path)
    print("\nDataset loaded successfully!")
    
    # Display descriptive statistics
    print("\nDescriptive Statistics:")
    descriptive_stats = compute_descriptive_stats(df)
    print(descriptive_stats)

    # Display available columns
    print("\nAvailable Columns:")
    available_columns = show_available_columns(df)
    print(available_columns)

    # Display information about the dataset
    print("\n Information about the dataset")
    df_info = info(df)
    print(df_info)
    
    # Interactive loop for user to choose options
    while True:
        print("\nChoose an option:")
        print("1. Plot Histogram")
        print("2. Plot Box Plot")
        print("3. Plot Scatter Plot")
        print("4. Compute Confidence Interval")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            column = input("Enter the column name for Histogram: ")
            if column in df.columns:
                plot_histogram(df, column)
            else:
                print("Invalid column name.")
                
        elif choice == '2':
            column = input("Enter the column name for Box Plot: ")
            if column in df.columns:
                plot_boxplot(df, column)
            else:
                print("Invalid column name.")
                
        elif choice == '3':
            column1 = input("Enter the first column name for Scatter Plot: ")
            column2 = input("Enter the second column name for Scatter Plot: ")
            if column1 in df.columns and column2 in df.columns:
                plot_scatter(df, column1, column2)
            else:
                print("Invalid column name(s).")
                
        elif choice == '4':
            column = input("Enter the column name for Confidence Interval: ")
            if column in df.columns:
                mean, lower, upper = compute_confidence_interval(df, column)
                print(f'Confidence Interval for {column} (95%): Mean = {mean}, CI = ({lower}, {upper})')
            else:
                print("Invalid column name.")
                
        elif choice == '5':
            print("Exiting the tool. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            
if __name__ == '__main__':
    main()