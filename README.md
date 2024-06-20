# EDA Tool

## Overview

This tool is designed to help users perform exploratory data analysis (EDA) interactively via the terminal. Users can load their dataset, compute descriptive statistics, and generate various visualizations to understand their data better.

Learning how to script repetitive tasks is useful as it mitigates the chance of human error. And such scripts are useful as they save time and effort.

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Usage](#usage)
   - [Run the Script](#1-run-the-script)
   - [Provide the Dataset File Path](#2-provide-the-dataset-file-path)
     - [How to Get the File Path](#how-to-get-the-file-path)
       - [Windows](#windows)
       - [Mac](#mac)
       - [Linux](#linux)
   - [Interact with the EDA Tool](#3-interact-with-the-eda-tool)
     - [Options Menu](#options-menu)
   - [Example Workflow](#example-workflow)

## Features

- **Descriptive Statistics**: Computes mean, median, mode, standard deviation, and quartiles for the dataset.
- **Visualizations**: Generates histograms, box plots, and scatter plots.
- **Inferential Statistics**: Calculates confidence intervals for sample means.

## Requirements

- pandas
- numpy
- matplotlib
- seaborn
- scipy

You can install these packages using pip:

```bash
pip install pandas numpy matplotlib seaborn scipy
```

or

```bash
pip3 install pandas numpy matplotlib seaborn scipy
```

## Usage

### 1. Run the Script

To start using the EDA Tool, you need to run the script using Python. Open your terminal or command prompt and navigate to the directory where the script is located. Then, execute the script with the following command:

```bash
python EDA_script.py
```

or

```bash
python3 EDA_script.py
```

### 2. Provide the Dataset File Path

After running the script, you will be prompted to enter the full path to your dataset (CSV file). Make sure you have the file path ready. Here are instructions to get the file path for different operating systems:

#### How to Get the File Path

##### Windows

1. Open File Explorer.
2. Navigate to the folder containing your dataset.
3. Hold the `Shift` key and right-click on the file.
4. Select `Copy as path`. This will copy the full file path to your clipboard.

##### Mac

1. Open Finder.
2. Navigate to the folder containing your dataset.
3. Hold the `Option` key and right-click on the file.
4. Select `Copy <filename> as Pathname`. This will copy the full file path to your clipboard.

##### Linux

1. Open your file manager.
2. Navigate to the folder containing your dataset.
3. Right-click on the file and select `Copy`.
4. Open a terminal and type `echo ` (note the space) and then paste the copied file path (usually `Ctrl + Shift + V`).

Paste the copied file path into the terminal when prompted.

### 3. Interact with the EDA Tool

Once the dataset is loaded successfully, the script will display the available columns and the descriptive statistics for the dataset. You can then choose from the following options:

#### Options Menu

1. **Show Available Columns**: Shows the columns in the dataset that can then be used for the other options.

2. **Plot Histogram**: Generates a histogram for a specified column to visualize the distribution of data.

   - You will be prompted to enter the column name for which you want to plot the histogram.

3. **Plot Box Plot**: Creates a box plot for a specified column to show the distribution of data and identify outliers.

   - You will be prompted to enter the column name for which you want to plot the box plot.

4. **Plot Scatter Plot**: Produces a scatter plot for two specified columns to visualize the relationship between them.

   - You will be prompted to enter the names of the two columns for the scatter plot (x-axis and y-axis).

5. **Compute Confidence Interval**: Calculates the confidence interval for the mean of a specified column.

   - You will be prompted to enter the column name for which you want to compute the confidence interval.

6. **Exit**: Exits the EDA tool.

### Example Workflow

Here is an example workflow for using the EDA Tool:

1. **Start the Script**:

   ```bash
   python EDA_script.py
   ```

2. **Enter the File Path**:

   ```
   Please enter the full path to your dataset (CSV file): /path/to/your/data.csv
   ```

3. **View Descriptive Statistics**:

   ```
   Descriptive Statistics:
                      Mean     Median     Mode  Standard Deviation Quartiles
   column1     123.456    120.000    110.0                15.678    (112.5, 123.0, 134.5)
   column2     78.910     75.000      70.0                10.111    (70.5, 75.0, 82.0)
   ```

   ```
   Available columns:
   column1 column2
   ```

4. **Choose an Option**:

   ```
   Choose an option:
   1. Plot Histogram
   2. Plot Box Plot
   3. Plot Scatter Plot
   4. Compute Confidence Interval
   5. Exit

   Enter your choice (1-5): 1
   ```

5. **Enter Column Name for Histogram**:

   ```
   Enter the column name for Histogram: column1
   ```

   (A histogram for `column1` will be displayed.)

6. **Repeat the Process** for other options as needed.

7. **Exit**:
   ```
   Enter your choice (1-5): 5
   Exiting the tool. Goodbye!
   ```

## Credit

Coded by Sophie Osiecki.
